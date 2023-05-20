#!/usr/bin/python3
""" A python script that starts a Flask web application and routes it
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return Hello HBNB!"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """Returns C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """Returns Python followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
    """Returns “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
