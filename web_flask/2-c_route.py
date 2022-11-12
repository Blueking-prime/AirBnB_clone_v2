#!/usr/bin/python3
''' A simple flask app'''
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Prints hello hbnb'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Prints hbnb'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    '''Prints c <text>'''
    text = escape(text)
    text_li = []
    for i in text:
        text_li.append(i)
    for i in range(len(text_li)):
        if text_li[i] == '_':
            text_li[i] = ' '
    text = ''.join(text_li)
    return 'C ' + text


if __name__ == '__main__':
    app.run(host='0.0.0.0')
