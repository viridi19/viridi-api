class RealData:
    def __init__(self, city):
        self.city = city

    def get_analisys(self):
        cities = self._robles_analisys()
        return cities
    
    def _robles_analisys(self):
        city = self.city
        return {
        "search":{
            "name": city,
            "match":[
                {
                    "name":"Fortaleza",
                    "similaridade":0.8,
                    "IDH":[
                        {
                            "name":"idh educacao",
                            "value":34.0
                        },
                        {
                            "name":"idh saude",
                            "value":25.0
                        }
                    ],
                    "climatic_events": self._jadson_analisys()
                },
                {
                    "name":"São Luis",
                    "similaridade":0.8,
                    "IDH":[
                        {
                            "name":"idh educacao",
                            "value":34.0
                        },
                        {
                            "name":"idh saude",
                            "value":25.0
                        }
                    ]
                }
            ],
            "IDH":[
                {
                    "name":"idh educacao",
                    "value":34.0
                },
                {
                    "name":"idh saude",
                    "value":25.0
                }
            ]
        }
    }

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