#!/usr/bin/python3
''' A simple flask app'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def display_states():
    '''Loads data into page'''
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def clean_up(exception):
    '''Removes the current sqlalchemy session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
