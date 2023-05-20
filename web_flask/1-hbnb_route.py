#!/usr/bin/python3
"""Script that starts a flask web application
Web app must be listening at 0.0.0.0, port 5000
Routes / display "Hello HBNB"
       /hbnb: display "HBNB"
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def route_hbnb():
    """ Prints Hello HBNB!"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints HBNB"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
