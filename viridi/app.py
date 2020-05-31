import os
from flask import Flask
from flask_restful import Api
from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher

from viridi.city_data import CityData

PORT = os.getenv('PORT', 5000)

_app = Flask(__name__)
API = Api(_app)

DISPATCHER = PathInfoDispatcher({'/': _app})
SERVER = WSGIServer(('0.0.0.0', PORT), DISPATCHER)

API.add_resource(CityData, '/data')
