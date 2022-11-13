#!/usr/bin/python3
''' A simple flask app'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    '''Prints hello hbnb'''
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    '''Removes the current sqlalchemy session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
