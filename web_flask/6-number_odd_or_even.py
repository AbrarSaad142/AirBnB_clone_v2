#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    display "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    display display “C ” followed by the value of the text variable
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/')
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """
    display “python” followed by the value of the text variable
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    display “number” followed by the value of the text variable
    """
    n = str(n)
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def html_number(n):
    """
    display “number” followed by the value of the text variable
    """
    n = str(n)
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    display “number” followed by the value of the text variable
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
