#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from os import environ
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def tearsown(exception):
    """emove the current SQLAlchemy Session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_list():
    """display page"""
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State),
                           cites=storage.all(City),
                           amenities=storage.all(Amenity))



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
