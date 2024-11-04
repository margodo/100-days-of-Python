# import os
import requests
from twilio.rest import Client

api_key_weather = ""
account_sid = ""
auth_token = ""

params = {
    "lat": 50.075539,
    "lon": 14.437800,
    "appid": api_key_weather,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=params)
response.raise_for_status()
weather_data = response.json()["list"]
precipitation = [item["weather"][0]["id"] for item in weather_data]
if precipitation[0] > 700:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {"https" : os.environ['https_proxy']}
    # client = Client(account_sid, auth_token,http_client=proxy_client)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain. Don't forget to bring an umbrella with you.",
        from_="+",
        to="+",
    )
print(message.status)