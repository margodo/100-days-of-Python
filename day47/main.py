from email.message import EmailMessage

import requests
from bs4 import *
import smtplib

TARGET_PRICE = 100
SMTP_ADDRESS =''
EMAIL = ''
PASSWORD = ''

url = 'https://appbrewery.github.io/instant_pot/'

response = requests.get(url=url,headers={'Accept-Language':'en-US,en;q=0.9'})
soup = BeautifulSoup(response.text,'html.parser')
price = float(soup.find(class_='a-price-whole').getText() + soup.find(class_='a-price-fraction').getText())
print(type(price))

if TARGET_PRICE > price:
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:IT is TIME\n\nFinally the price is perfect fot the purchase ${price}.\n{url}".encode("utf-8")
        )