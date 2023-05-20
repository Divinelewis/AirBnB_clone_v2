#!/usr/bin/python3
"""Script that starts a Flask web application:
Web app is listening on 0.0.0.0, port 5000
Route:
    / - display 'Hello HBNB!'
    /hbnb - display 'HBNB'
    /c/<text> - display 'C' followed by the value of the text variable (replace underscore _ symbol with a space)
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """prints Hello HBNB!"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Prints HBNB"""
    return ("HBNB")


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """prints C followed by <text> content"""
    text = text.replace("_", " ")
    return "C %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
