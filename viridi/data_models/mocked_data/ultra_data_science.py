class MockedData:

    def __init__(self, city):
        self.city = city
    
    def do_stuff(self):
        self.covid_data = {
            'cases': 123456,
            'deaths': 123,
        }

        self.climate_data = {
            'humidity': 100,
            'temperature': 30,
        }

        self.soc_eco_data = {
            'hdi': 0.87,
            'population': 120000,
        }

        self.similar_cities = {
            'city1':{
                'name': 'Pindamonhagaba',
                'cases': 111222
            },
            'city2':{
                'name': 'Cracolandia',
                'cases': 111222
            }
        }
