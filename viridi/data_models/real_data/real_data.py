import json

from flask_restful import abort

from viridi.resources.anomaly_humid_points import ANOMALY_HUMID
from viridi.resources.anomaly_prec_points import ANOMALY_PREC
from viridi.resources.anomaly_temp_points import ANOMALY_TEMP
from viridi.resources.climatic_similarity import CLIMATIC_SIMILARITY


class RealData:
    def __init__(self, city):
        self.city = city
        self.coordinates = {
                    "data": [
                        { "name": "Rio Branco", "coordinates": [-67.8662019, -9.9862442] },
                        { "name": "Maceió", "coordinates": [-35.7568902, -9.5943984] },
                        { "name": "Macapá", "coordinates": [0.1019439, -51.1670724] },
                        { "name": "Manaus", "coordinates": [-60.1075319, -3.0443101] },
                        { "name": "Salvador", "coordinates": [-38.490317, -12.9015883] },
                        { "name": "Fortaleza", "coordinates": [-38.5891584, -3.7899266] },
                        { "name": "Brasília", "coordinates": [-48.0779611, -15.7744219] },
                        { "name": "Vitória", "coordinates": [-49.4446947, -16.6954997] },
                        { "name": "Goiânia", "coordinates": [-48.0779611, -15.7744219] },
                        { "name": "São Luís", "coordinates": [-44.4383634, -2.6271281] },
                        { "name": "Cuiabá", "coordinates": [-48.0779611, -15.7744219] },
                        { "name": "Campo Grande", "coordinates": [-54.7057456, -20.4809249] },
                        { "name": "Belo Horizonte", "coordinates": [-44.0342617, -19.9025411] },
                        { "name": "Belém", "coordinates": [-48.5205932, -1.3411793] },
                        { "name": "João Pessoa", "coordinates": [-34.9518092, -7.1464332] },
                        { "name": "Recife", "coordinates": [-49.4302249, -25.4947398] },
                        { "name": "Teresina", "coordinates": [-42.8112899, -5.0935648] },
                        { "name": "Rio de Janeiro", "coordinates": [-43.7268521, -22.9132513] },
                        { "name": "Natal", "coordinates": [-35.2924559, -5.7997438] },
                        { "name": "Porto Alegre", "coordinates": [-51.3175682, -30.1084984] },
                        { "name": "Porto Velho", "coordinates": [-63.8900121, -8.7564592] },
                        { "name": "Boa Vista", "coordinates": [-36.2463902, -7.2660776] },
                        { "name": "Florianópolis", "coordinates": [-48.7511475, -27.5707043] },
                        { "name": "São Paulo", "coordinates": [-46.8761689, -23.6815303] },
                        { "name": "Aracaju", "coordinates": [-37.1733679, -11.0058313] },
                        { "name": "Palmas", "coordinates": [-48.417446, -10.2598832] }
                    ]
                }

    def get_analisys(self):
        search = self._robles_analisys(self.city)
        search = search['search']
        cities = {}
        cities['searched_city'] = search['name']
        cities['coord_city'] = self._find_coord(cities['searched_city'])
        cities['IDH'] = search['IDH']
        cities['climate'] = []
        cities['similar'] = search['match']

        for _item in cities['similar']:
            _item['coord_city'] = self._find_coord(_item['name'])
            item = _item
            item['climate'] = []
            climate = self._jadson_analisys(cities['searched_city'], item['name'])
            cities['similarity_temp'] = climate['similarity_temp']
            cities['similarity_humid'] = climate['similarity_humid']
            cities['similarity_prec'] = climate['similarity_prec']
            item['similarity_temp'] = climate['similarity_temp']
            item['similarity_humid'] = climate['similarity_humid']
            item['similarity_prec'] = climate['similarity_prec']
            cities['climate'] = climate[cities['searched_city']]
            item['climate'] = climate[item['name']]
        return cities

    def _robles_analisys(self, city):
        # Algorithm
        data = {
            "search": {
                "name": city,
                "IDH": [
                        {
                            "name": "idh educacao",
                            "value": 34.0
                        },
                        {
                            "name": "idh saude",
                            "value": 25.0
                        }
                    ],    
                "match": [
                    {
                        "name": "Fortaleza",
                        "similarity_rate": 467.0,
                        "IDH": [
                            {
                                "name": "idh educacao",
                                "value": 34.0
                            },
                            {
                                "name": "idh saude",
                                "value": 25.0
                            }
                        ]
                    },
                    {              
                        "name": "Porto Alegre",
                        "similarity_rate": 467.0,
                        "IDH": [
                            {
                                "name": "idh educacao",
                                "value": 34.0
                            },
                            {
                                "name": "idh saude",
                                "value": 25.0
                            }
                        ]
                    },
                ]
            }
        }
        return data 

    def _jadson_analisys(self, city1, city2=None):

        results = CLIMATIC_SIMILARITY[city1][city2]

        # insert results to city1
        results[city1] = ANOMALY_TEMP[city1]
        results[city1].update(ANOMALY_HUMID[city1])
        results[city1].update(ANOMALY_PREC[city1])

        # insert results to city2
        results[city2] = ANOMALY_TEMP[city2]
        results[city2].update(ANOMALY_HUMID[city2])
        results[city2].update(ANOMALY_PREC[city2])

        return results

    def _find_coord(self, city):
        coords = self.coordinates['data']
        for item in coords:
            if city == item['name']:
                return item['coordinates']
        abort(404)




