from flask import Flask
from flask_restful import Api
from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher

from viridi.city_data import CityData


APP = Flask(__name__)
API = Api(APP)

DISPATCHER = PathInfoDispatcher({'/': APP})
SERVER = WSGIServer(('0.0.0.0', 8080), DISPATCHER)

API.add_resource(CityData, '/')

if __name__ == '__main__':
    print('Running on port 8080')
    SERVER.safe_start()
