# import json

from flask_restful import abort

# from viridi.resources.anomaly_humid_points import ANOMALY_HUMID
# from viridi.resources.anomaly_prec_points import ANOMALY_PREC
# from viridi.resources.anomaly_temp_points import ANOMALY_TEMP
# from viridi.resources.climatic_similarity import CLIMATIC_SIMILARITY


class MockedData:
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
            cities['similarity_rate_temp'] = climate['similarity_rate_temp']
            cities['similarity_rate_humid'] = climate['similarity_rate_humid']
            item['similarity_rate_temp'] = climate['similarity_rate_temp']
            item['similarity_rate_humid'] = climate['similarity_rate_humid']
            cities['climate'] = climate['city1']
            item['climate'] = climate['city2']
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

    @staticmethod
    def _jadson_analisys():
        return {
            "similarity_rate_temp": 0.8, # similaridade geral entre as series temporais de temp
            "similarity_rate_humid": 0.85, # similaridade geral entre as series temporais de humid
            "city1": {
                "timeseries_temp": [30.5, 46.1, 21.7, 83.9], # lista de decimais que representam temperatura media (pode fazer uma lista de uns 90 pontos),
                "anomalous_points_temp": [1, 3], # lista de pontos que podem indicar anomalias no clima (lista pode ser vazia e os numeros representam o indice da timeseries)
                "timeseries_humid": [70.5, 66.1, 89.7, 83.9], # lista de decimais que representam humidade media (pode fazer uma lista de uns 90 pontos),
                "anomalous_points_humid": [], # lista de pontos que podem indicar anomalias na humidade (lista pode ser vazia e os numeros representam o indice da timeseries)
                "date_range": ["2020-01-01", "2020-01-02", "2020-01-03", "2020-01-04"]
            },
            "city2": {
                "timeseries_temp": [31.5, 45.1, 21.5, 23.7], # lista de decimais que representam temperatura media (pode fazer uma lista de uns 90 pontos),
                "anomalous_points_temp": [1], # lista de pontos que podem indicar anomalias no clima (lista pode ser vazia e os numeros representam o indice da timeseries)
                "timeseries_humid": [71.5, 65.1, 84.7, 83.5], # lista de decimais que representam humidade media (pode fazer uma lista de uns 90 pontos),
                "anomalous_points_humid": [], # lista de pontos que podem indicar anomalias na humidade (lista pode ser vazia e os numeros representam o indice da timeseries)
                "date_range": ["2020-01-04", "2020-01-05", "2020-01-06", "2020-01-07"]
            }
        }

    def _find_coord(self, city):
        coords = self.coordinates['data']
        for item in coords:
            if city == item['name']:
                return item['coordinates']
        abort(404)
