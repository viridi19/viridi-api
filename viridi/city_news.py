from flask import request
from flask_restful import Resource

from viridi.utils import query_news

# from google_search_results import GoogleSearchResults


class CityNews(Resource):
    @staticmethod
    def post():
        city = request.form['city']
        res = query_news(city)

        return res, 200
