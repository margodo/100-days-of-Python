from flask import Flask, render_template, url_for
from post import Post
import requests

app = Flask(__name__)
posts_api = requests.get('https://api.npoint.io/2ddcb93f2cb95e21e191')
posts = posts_api.json()

posts_list = []
for post in posts:
    new_post = Post(post["id"],post["title"],post["subtitle"],post["body"])
    posts_list.append(new_post)

@app.route('/')
def home():
    global posts
    return render_template("index.html", posts = posts_list)

@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for post_chosen in posts_list:
        if post_chosen.id == index:
            requested_post = post_chosen
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
