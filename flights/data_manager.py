import requests

from flight_search import FlightSearch
from pprint import pprint

class DataManager:
    # CHEKING IF CONNECTION TO MY SHEETS IS VALID
    google_sheets_endpoint = "https://api.sheety.co/53d449493963c132cc67a889a7d62c4f/flightDeals/prices"
    response1 = requests.get(url=google_sheets_endpoint)
    sheet_data = response1.json()['prices']


    # <----- CHECK CONSOLE FOR STATUS CODE

    # POST METHOD TO THE GOOGLE SHEETS.
    # POST_ENDPOINT = "https://api.sheety.co/53d449493963c132cc67a889a7d62c4f/flightDeals/prices/2"
    # body = {
    #     "price": [{
    #         "city": "East LA",
    #         "iataCode": '',
    #         "id": '3',
    #         "lowestPrices": "15"
    #     }]
    # }
    #
    # response = requests.post(url=POST_ENDPOINT, params=body)
    #
    # print(response.text)
