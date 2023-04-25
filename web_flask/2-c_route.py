#!/usr/bin/python3
""" A script that starts a flask we application """
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
