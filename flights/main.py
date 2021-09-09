import os
from pprint import pprint

from data_manager import DataManager
# from flight_search import FlightSearch
# from notification_manager import NotificationManager

# notifications = NotificationManager()
# flight_search = FlightSearch()
sheet_data = DataManager().sheet_data

pprint(sheet_data)
