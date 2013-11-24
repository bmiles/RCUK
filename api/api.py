from json import dumps
from os import environ
import sys

from bson import json_util
from eve import Eve
from flask import make_response, send_from_directory

from people_search import search as people_search
from people_search import search_in_orcid as orcid_search
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
    return make_response(dumps(people_search(topic), default=json_util.default))

@app.route('/orcid/<path:names>')
def orcid(name):
    return search_in_orcid(name)

if __name__ == '__main__':
    # Heroku support: bind to PORT if defined, otherwise default to 5000.
    if 'PORT' in environ:
        port = int(environ.get('PORT'))
        host = '0.0.0.0'
    else:
        port = 5000
        host = '127.0.0.1'
    app.run(host=host, port=port)
