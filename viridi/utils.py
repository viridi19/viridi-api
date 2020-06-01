import requests
import json
from datetime import datetime
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions, SentimentOptions


VALID_WORDS = ["corona", "covid", "morte", "pandemia", "mascara", "covid19", "covid-19", "hospitais", "pulmão", "pulmões", "coronavírus", "mortes", "distanciamento"]
INVALID_WORDS = ["treino", "treinos", "futebol", "bola", "jogador", "jogadores", "jogos"]


def query_category(url):
  authenticator = IAMAuthenticator('<API_KEY>')
  natural_language_understanding = NaturalLanguageUnderstandingV1(version='2019-07-12',authenticator=authenticator)

  natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/fe6a1388-3862-495d-bde1-c51135a37fff')

  words_res = natural_language_understanding.analyze(
    url=url,
    features=Features(sentiment=SentimentOptions(),
                      keywords=KeywordsOptions(sentiment=True,emotion=True,limit=2))
                      ).get_result()

  return {"sentiment": words_res["sentiment"], "keywords": words_res["keywords"]}


def query_news(city):
    city = city.strip()
    url = (f'https://newsapi.org/v2/everything?domains=terra.com.br,uol.com.br,globo&q={city}&pageSize=12&apiKey=<API_KEY>')

    response = ''
    n_res = {
      "filled": False,
      "author": '',
      "title": '',
      "description": '',
      "url": '',
      "urlToImage": '',
      "publishedAt": '',
    }
    
    response = requests.get(url).json()

    articles = response["articles"]
    sorted_articles = sorted(articles, key=lambda x: datetime.strptime(x['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'))

    for article in sorted_articles:
        if __valid_new(article):
            n_res["filled"] = True
            n_res["author"] = article["author"]
            n_res["title"] = article["title"]
            n_res["description"] = article["description"]
            n_res["url"] = article["url"]
            n_res["urlToImage"] = article["urlToImage"]
            n_res["publishedAt"] = article["publishedAt"]

    

    return n_res


def __valid_new(new):
    for vw in VALID_WORDS:
        for iw in INVALID_WORDS:
            title = new["title"].lower()
            description = new["description"]
            if vw in title and iw not in title:
                return True
            if vw in description and iw not in description:
                return True
    return False
