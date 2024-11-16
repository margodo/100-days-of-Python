from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphesis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
def home():
    return "<h1 style='text-align: center'>Hello, Flask!</h1>\
            <p>This is my web</p>\
            <img src='https://user-images.githubusercontent.com/6876788/96633009-d1818000-1318-11eb-9f1d-7f914f4ccb16.gif' width=200px,heught=200px>"

@app.route("/farewell")
@make_bold
@make_emphesis
@make_underlined
def say_bye():
    return "Bye! Have a great day!"

@app.route("/<name>/<int:numb>")
def greet(name,numb):
    return f'Hello {name}. {numb}'

if __name__ == '__main__':
    app.run(debug=True)

# Passing args to decorator

# def is_authenticated(function):
#     def wrapper(*args,**kwargs):
#         if args[0].logged_in == True:
#             function(args[0])
#     return wrapper

# class User:
#     def __init__(self,name):
#         self.name = name
#         self.logged_in = False

# @is_authenticated
# def create_post(user):
#     print(f'{user.name} has just posted')

# new_user = User('Alex')
# new_user.logged_in = True
# create_post(new_user)