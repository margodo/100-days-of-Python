from flask import Flask, render_template, request
import requests

posts = requests.get("https://api.npoint.io/ca2d1d75fb0b2b9d04f6").json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        data = request.form
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
