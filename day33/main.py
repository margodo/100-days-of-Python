import requests
from datetime import datetime
import smtplib

MY_LAT = 50.075539
MY_LONG = 14.437800

my_email = "ergaliaf0390@gmail.com"
password = "wtxhiclaiwsdembz"

def check_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lng = float(data["iss_position"]["longitude"])
    iss_lat = float(data["iss_position"]["latitude"])
    if MY_LAT-5 < iss_lat < MY_LAT + 5 and MY_LONG-5 < iss_lng < MY_LONG+5:
        return True

def check_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted":0
    }
    sunset_sunrise_api = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sunset_sunrise_api.raise_for_status()
    data = sunset_sunrise_api.json()
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split('T')[1].split(":")[0])
    time_now = datetime.now()
    hour = time_now.hour
    if hour < sunrise or hour > sunset:
        return True

if check_time() and check_location():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="timmytimmy456@yahoo.com",msg = f"Subject: Hey Space Station location is there!\n\nYou can look out and see space station.")