from flask import request
from flask_restful import Resource

from viridi.data_models.mocked_data.ultra_data_science import MockedData

# from serpapi.google_search_results import GoogleSearchResults

class CityData(Resource):
    @staticmethod
    def post():
        city = request.form['city']
        data = MockedData(city)
        data.do_stuff()
        res = {
            'city': data.city,
            'covid_data': data.covid_data,
            'climate_data': data.climate_data,
            'soc_eco_data': data.soc_eco_data,
            'similar_cities': data.similar_cities
        }

        return res, 200
