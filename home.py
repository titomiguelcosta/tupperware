from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! It works. Here we go."

@app.route("/bye")
def bye():
    return "See you again soon!"
