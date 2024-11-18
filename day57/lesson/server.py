from flask import Flask, render_template
import random
import datetime
import requests

url_age = 'https://api.agify.io'
url_gender = 'https://api.genderize.io'
app = Flask(__name__)

@app.route('/')
def welcome():
    today = datetime.date.today().year
    rand_numb = random.randint(0,10)
    return render_template('index.html',numb = rand_numb, today=today)

@app.route('/guess/<name>')
def guess_name(name):
    params = {
        'name': name
    }
    response_age = requests.get(url=url_age,params=params)
    response_age.raise_for_status()
    age_data = response_age.json()["age"]
    response_gender = requests.get(url=url_gender,params=params)
    gender_data = response_gender.json()["gender"]
    return render_template('name.html',name=name, age=age_data, gender=gender_data)

@app.route('/blog/<num>')
def blog(num):
    data = requests.get(url='https://api.npoint.io/2ddcb93f2cb95e21e191')
    posts = data.json()
    return render_template('blog.html', posts = posts)

if __name__ == '__main__':
    app.run(debug=True)