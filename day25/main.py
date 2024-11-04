# with open("weather_data.csv") as weather:
#     data = weather.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
from numpy.ma.core import squeeze
from pandas.io.common import file_path_to_url

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)
#
# # Get row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# print(monday.temp +32)

# Create data frame from scratch
# data_dict = {
#     "students": ["amy","lore", "alex"],
#     "score": [76,52,84]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

squirrels = pandas.read_csv("squirrel_nyc.csv")
gray_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
white_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Black"])
print(gray_squirrels)
squirrel_dict = {
    "Fur": ["Gray","Cinnamon", "Black"],
    "Quiantity": [gray_squirrels,cinnamon_squirrels,white_squirrels]
}
data = pandas.DataFrame(squirrel_dict)
data.to_csv("squirrel_count.csv")