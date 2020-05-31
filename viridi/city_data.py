from flask import request
from flask_restful import Resource

from viridi.data_models.real_data.real_data import RealData


class CityData(Resource):
    @staticmethod
    def post():
        city = request.form['city']
        data = RealData(city)
        res = data.get_analisys()

        return res, 200
