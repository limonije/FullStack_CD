# Import what we need from flask
from flask import Flask

# Create a Flask app inside 'app'
app = Flask(__name__)


# Assign a function to be called when the path '/' is requested
@app.route('/')
def index():
    return "<h1>Home, sweet home.</h1>"


@app.route('/winc')
def winc():
    return "<h1>Hello, Winc Academy!</h1>"


@app.route('/succes')
def succes():
    return "<h1>Deployment is een succes</h1>"
