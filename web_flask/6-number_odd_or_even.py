#!/usr/bin/python3
''' A simple flask app'''
from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
def python_is_default():
    '''Prints "Python is cool"'''
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    '''Prints Python <text>'''
    text = escape(text)
    text = text.replace('_', ' ')
    return 'Python ' + text


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    '''Prints n if number'''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number_template(n):
    '''diplays page if n is a number'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_number_odd_or_even(n):
    '''diplays page if n is a number'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
