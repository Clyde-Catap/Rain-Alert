import requests
import os
from twilio.rest import Client

api_key = "0e7f3885637e1549e143e0c012dd5258"
Latitude = 16.043859
Longitude = 120.335190

msg = "Bring Umbrella Dumbass"
account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]

parameters = {
    "lat": 16.043859,
    "lon": 120.335190,
    "appid": api_key


}

will_rain = False

data = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
data_json = data.json()
x = data_json["list"]

for gg in range(6):
    w = (x[gg]["weather"][0]["id"])
    if w > 700:
        will_rain = True


if will_rain:
    # Find your Account SID and Auth Token in Account Info and set the environment variables.
    # See http://twil.io/secure
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      body=msg,
      from_='+16086315618',
      to='+639292937967'
    )



