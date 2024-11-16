from flask import Flask
app = Flask(__name__)
import random

rand_numb = random.randint(0,9)

@app.route("/")
def home():
    return "<h1>'Guess a number between 0 and 9'</h1>\
            <img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXVmNHpsa2Q0d2hrdWp4azVxOWVvMnM2OHBkMTJ2c3YyZThhdmxqaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IwAZ6dvvvaTtdI8SD5/giphy.gif' width=400px,heught=400px>"

@app.route("/<numb>")

def numb_page(numb):

    global rand_numb
    if int(numb) < rand_numb:
        return "<h1 style='color:red'>'Too low, try again!'</h1>\
                <img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmoxcjRxdjM1aGVsa3d1dGJ0eDYzYTF5c2R1bGE0b2x5eHQwOXUzdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vVzH2XY3Y0Ar6/giphy.gif' width = 400px,height=400px>"
    elif int(numb) > rand_numb:
        return "<h1 style='color:violet'>'Too high, try again!'</h1>\
                <img src= 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXIzZ3RkYXY1b2NxNG01Z2h0azQ4d2xweTRsZnJhMTVicjR2bjAydSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KEh5kliRTSVJm/giphy.gif' width=400px,height=400px>"
    else:
        return "<h1 style='color:green'>'You got it right!'</h1>\
             <img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWRnYXF4aTBlcTkzbHl0ZXMxbmhwcmNjZWZ3cnc4bGk0eGJkaTBweSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/12UMzHiF9w3LGg/giphy.gif' width=400px,height=400px>"


if __name__ == '__main__':
    app.run(debug=True)

