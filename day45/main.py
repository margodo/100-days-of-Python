from bs4 import BeautifulSoup
import requests

response = requests.get("web")

movies_page = response.text

soup = BeautifulSoup(movies_page,'html.parser')

titles = soup.find_all('h3',class_='title')
title_formatted = [movie.getText() for movie in titles]
movies = title_formatted[::-1]

with open('movies.txt', mode='w',encoding='utf-8') as file:
    for movie in movies:
        file.write(f'{movie}\n')

