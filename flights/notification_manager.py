import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

TWILIO_NUMBER = "ENTER YOUR TWILIO NUMBER HERE"

os.environ['TWILIO_ACCOUNT_SID']='ENTER YOUR ACCOUNT SID HERE'
os.environ['TWILIO_AUTH_TOKEN']='ENTER YOUR AUTH TOKEN HERE'

class NotificationManager:
    proxy_client = TwilioHttpClient()
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    print(type(account_sid))
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(body="This is Juan from the reverse world, please help him",
                                     from_=TWILIO_NUMBER,
                                     to="2138422717")

    print("everything went through")
