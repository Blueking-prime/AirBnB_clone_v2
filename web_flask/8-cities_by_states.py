#!/usr/bin/python3
''' A simple flask app'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_states():
    '''Prints hello hbnb'''
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def clean_up(exception):
    '''Removes the current sqlalchemy session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
