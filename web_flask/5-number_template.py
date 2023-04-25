#!/usr/bin/python3
""" A script that starts a flask we application """
from flask import Flask, render_template

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def home_page():
    """" Show a message when accessed """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_page():
    """ Displays hbnb when accessed """
    return 'HBNB'


@app.route('/c/<text>')
def text_route(text):
    """ display a custom text """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_route(text='is cool'):
    """ Display aa custom text if text is assigned """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_route(n):
    """ Display number in path variable """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Display HTML page """
    return render_template("5-number.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
