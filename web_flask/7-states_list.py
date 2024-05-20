#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def tearsown(exception):
    """emove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display page"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=storage.all(State))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
