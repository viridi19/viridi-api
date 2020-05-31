from flask import request
from flask_restful import Resource

# from viridi.data_models.real_data.real_data import RealData
from viridi.data_models.mocked_data.mocked_data import MockedData


class CityData(Resource):
    @staticmethod
    def get():
        city = request.args.get('city')
        # data = RealData(city)
        data = MockedData(city)
        res = data.get_analisys()

        return res, 200
