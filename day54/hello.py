from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/farewell")
def say_bye():
    return "Bye! Have a great day!"

if __name__ == '__main__':
    app.run()

# Python Decorator

# import time

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#     return wrapper_function

# @delay_decorator
# def say_hello():
#     print('Hello')

# @delay_decorator
# def say_bye():
#     print('Bye')

# say_hello()