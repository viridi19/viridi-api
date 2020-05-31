import requests
import json
from datetime import datetime

MOCKED = False
VALID_WORDS = ["corona", "covid", "morte", "pandemia", "mascara", "covid19", "covid-19", "hospitais", "pulmão", "pulmões", "coronavírus", "mortes", "distanciamento"]
INVALID_WORDS = ["treino", "treinos", "futebol", "bola", "jogador", "jogadores", "jogos"]

def query_news(city):
    city = city.strip()
    url = (f'https://newsapi.org/v2/everything?domains=terra.com.br,uol.com.br,globo&q={city}&pageSize=12&apiKey=5c3349b9af944d3a8838be33a30ca9e8')

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
    if not MOCKED:
        response = requests.get(url).json()
    else:
        with open("./news_example.json") as f:
            response = json.load(f)

    articles = response["articles"]
    sorted_articles = sorted(articles, key=lambda x: datetime.strptime(x['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'))

    for article in sorted_articles:
        if __valid_new(article):
            n_res["filled"] = False
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
