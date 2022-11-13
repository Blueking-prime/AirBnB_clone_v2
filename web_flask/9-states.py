#!/usr/bin/python3
''' A simple flask app'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_states():
    '''Prints hello hbnb'''
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_state(id):
    '''Prints hello hbnb'''
    states = storage.all('State')
    for state in states.values():
        if id == state.id:
            cities = state.cities
        else:
            cities = None
    return render_template('9-states.html', cities=cities)


@app.teardown_appcontext
def clean_up(exception):
    '''Removes the current sqlalchemy session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
