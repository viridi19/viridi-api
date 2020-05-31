from flask import request
from flask_restful import Resource


class CityNews(Resource):
    @staticmethod
    def get(self):
        print(request.form['city'])
        month = 4
        from_day = 2
        to_day = 3
        year = 2020

        params = {
            "engine": "google",
            "q": "Trump",
            "google_domain": "google.com",
            "tbm": "nws",
            "tbs": f"cdr:1,cd_min:{month}/{from_day}/{year},cd_max:{month}/{to_day}/{year}",
        }

        client = {} # GoogleSearchResults(params)
        data = [] # client.get_dict()

        print("News results")

        for result in data['news_results']:
            print(f"""
        Title: {result['title']}
        Snippet: {result['snippet']}
        Date: {result['date']}
        """)    

        return {}, 200
