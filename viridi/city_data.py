from flask import request
from flask_restful import Resource

# from viridi.data_models.real_data.real_data import RealData
from viridi.data_models.real_data.real_data import RealData


class CityData(Resource):
    @staticmethod
    def get():
        city = request.args.get('city')
        # data = RealData(city)
        data = RealData(city)
        res = data.get_analisys()

        return res, 200
