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

    # def get(self):
    #     print(request.form['city'])
    #     month = 4
    #     from_day = 2
    #     to_day = 3
    #     year = 2020

    #     params = {
    #         "engine": "google",
    #         "q": "Trump",
    #         "google_domain": "google.com",
    #         "tbm": "nws",
    #         "tbs": f"cdr:1,cd_min:{month}/{from_day}/{year},cd_max:{month}/{to_day}/{year}",
    #     }

    #     client = GoogleSearchResults(params)
    #     data = client.get_dict()

    #     print("News results")

    #     for result in data['news_results']:
    #         print(f"""
    #     Title: {result['title']}
    #     Snippet: {result['snippet']}
    #     Date: {result['date']}
    #     """)    

    #     return None, 200
