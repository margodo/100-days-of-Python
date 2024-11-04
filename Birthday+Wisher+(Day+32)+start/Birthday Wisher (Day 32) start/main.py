import datetime as dt
import smtplib
import random


now = dt.datetime.now()
week_day = now.weekday()
my_email = "ergaliaf0390@gmail.com"
password = "wtxhiclaiwsdembz"

if week_day == 0:
    with open("quotes.txt") as file:
        motivation = file.readlines()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="timmytimmy456@yahoo.com",msg = f"Subject: Monday Motivation\n\n{random.choice(motivation)}")


# year = now.year
# if year == 2024:
#     print("Yeeey")
# print(week_day)
# date_of_birth = dt.datetime(year=2000,month=8,day=9,hour=2,minute=30)
# print(date_of_birth)