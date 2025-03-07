#!/usr/bin/python3
''' A simple flask app'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Prints hello hbnb'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Prints hbnb'''
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
