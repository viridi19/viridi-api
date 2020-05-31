from flask import request
from flask_restful import Resource

from viridi.utils import query_news, query_category

# from google_search_results import GoogleSearchResults

MOCK = True
class CityNews(Resource):
    @staticmethod
    def get():
        res = ''
        if not MOCK:
            city = request.form['city']
            news_res = query_news(city)
            _url = news_res["url"]
            nlu_res = query_category(_url)

            res = {
                "news": news_res,
                "nlu": nlu_res
            }
        else:
            res = MOCK_DATA

        return res, 200

MOCK_DATA = {
  "news": {
    "filled": True,
    "author": "Estadão Conteúdo",
    "title": "Com 25 mortes por coronavírus, sistema prisional continuará sem visita em SP",
    "description": "Segundo a Secretaria de Administração Penitenciária, 12 óbitos são de detentos e 13 de funcionários",
    "url": "https://www.terra.com.br/vida-e-estilo/saude/com-25-mortes-por-coronavirus-sistema-prisional-continuara-sem-visita-em-sp,75337fb53658d9b9dadd8cb8c3604c28diu4ea5f.html",
    "urlToImage": "http://p2.trrsf.com/image/fget/cf/800/450/middle/s1.trrsf.com/atm/3/core/_img/terra-logo-white-bg-v3.jpg",
    "publishedAt": "2020-05-29T23:58:13Z"
  },
  "nlu": {
    "sentiment": {
      "document": {
        "score": -0.735565,
        "label": "negative"
      }
    },
    "keywords": [
      {
        "text": "Secretaria de Administração Penitenciária",
        "sentiment": {
          "score": 0,
          "label": "neutral"
        },
        "relevance": 0.825666,
        "count": 1
      },
      {
        "text": "total de servidores",
        "sentiment": {
          "score": 0,
          "label": "neutral"
        },
        "relevance": 0.656973,
        "count": 1
      }
    ]
  }
}