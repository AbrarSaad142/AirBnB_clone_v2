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


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page with a list of all State objects sorted by name"""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('9-states.html', states=states, state=None)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display a HTML page"""
    states = storage.all(State).values()
    state = None
    for x in states:
        if x.id == id:
            state = x
            break
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states.html', states=None,
                               state=state, cities=cities)
    else:
        return render_template('9-states.html', states=None,
                               state=None, cities=None)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
