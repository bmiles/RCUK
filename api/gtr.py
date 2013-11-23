from datetime import datetime
from logging import getLogger, DEBUG, debug
from os import environ
from sys import maxint

from pymongo import MongoClient
import requests

dbname = environ['MONGOLAB_URI'].rsplit('/', 1)[1]
db = MongoClient(environ['MONGOLAB_URI'])[dbname]


def convert_date(dct, field):
    dct[field] = datetime.fromtimestamp(dct[field]/1000)


def request(url, params=None, headers=None):
    r = requests.get(url + '.json', params=params, headers=headers)
    if not r.status_code == 200:
        raise RuntimeError(r.json())
    return r.json()


def populate_project(url):
    project = db.projects.find_one({"href": url})
    if not project:
        data = request(url)
        convert_date(data, 'created')
        # FIXME: This would be ideal, but Eve doesn't like it
        # data['_id'] = data.pop('id')
        return db.projects.insert(data)
    return project['_id']


def populate_organisation(url):
    organisation = db.organisations.find_one({"href": url})
    if not organisation:
        data = request(url)
        convert_date(data, 'created')
        for address in data['addresses']['address']:
            convert_date(address, 'created')
        # FIXME: This would be ideal, but Eve doesn't like it
        # data['_id'] = data.pop('id')
        return db.organisations.insert(data)
    return organisation['_id']


rel2func = {
    'PI_PER': populate_project,
    'COI_PER': populate_project,
    'FELLOW_PER': populate_project,
    'PM_PER': populate_project,
    'EMPLOYED': populate_organisation
}


def populate_db(page=1, size=100, end=maxint):

    def append_rel(rel, url, person):
        if not rel in person:
            person[rel] = []
        # FIXME: should be: person[rel].append(rel2func[rel](url))
        person[rel].append(rel2func[rel](url))

    def get_person(person):
        convert_date(person, 'created')
        for link in person['links']['link']:
            append_rel(link['rel'], link['href'], person)
        return person

    total = 1
    while page <= min(end, total):
        payload = {'p': page, 's': size}
        data = request('http://gtr.rcuk.ac.uk/gtr/api/persons', payload)
        persons = [get_person(person) for person in data['person']]
        ids = db.persons.insert(persons)
        debug("On page %d, inserted persons %s" % (page, ids))
        page = data['page'] + 1
        total = data['totalPages']

if __name__ == '__main__':
    getLogger().setLevel(DEBUG)
    populate_db()
