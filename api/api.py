from os import environ
import sys

from eve import Eve
from flask import jsonify, send_from_directory

from people_search import search as people_search
from settings import API_NAME

app = Eve(API_NAME)


@app.route('/scripts/<path:filename>')
def scripts(filename):
    return send_from_directory(app.root_path + '/app/dist/scripts/', filename)


@app.route('/styles/<path:filename>')
def styles(filename):
    return send_from_directory(app.root_path + '/app/dist/styles/', filename)


@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory(app.root_path + '/app/dist/images/', filename)


@app.route('/views/<path:filename>')
def views(filename):
    return send_from_directory(app.root_path + '/app/dist/views/', filename)


@app.route("/")
def index():
    return send_from_directory(app.root_path + '/app/dist/', 'index.html')


@app.route('/search/<path:topic>')
def search(topic):
    return jsonify(**people_search(topic))


if __name__ == '__main__':
    # Heroku support: bind to PORT if defined, otherwise default to 5000.
    if 'PORT' in environ:
        port = int(environ.get('PORT'))
        host = '0.0.0.0'
    else:
        port = 5000
        host = '127.0.0.1'
    app.run(host=host, port=port)
