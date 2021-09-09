import requests

API_KEY = "ENTER YOUR TEQUILA API KEY HERE"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/location/query"
        headers = {'apikey': API_KEY}
        query = {'term': city_name, 'location_types': 'city'}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        print(response.text)
        results = response.json()['locations']
        code = results[0]['code']
        print(results)
        print(code)
        return code
