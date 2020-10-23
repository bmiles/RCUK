from datetime import datetime
from logging import getLogger, DEBUG, debug
from os import environ
from sys import maxsize

from pymongo import MongoClient
import requests

dbname = environ['MONGOLAB_URI'].rsplit('/', 1)[1]
db = MongoClient(environ['MONGOLAB_URI'])[dbname]


class FailedRequest(Exception):
    pass


def convert_date(dct, created, updated):
    dct[created] = datetime.fromtimestamp(dct[created]/1000)
    if dct[updated]:
        dct[updated] = datetime.fromtimestamp(dct[updated]/1000)
    else:
        dct[updated] = dct[created]


def request(url, params=None, headers=None):
    debug("Querying %s.json with params %r and headers %r" %
          (url, params, headers))
    r = requests.get(url + '.json', params=params, headers=headers)
    if not r.status_code == 200:
        raise FailedRequest(r.json())
    return r.json()


def populate_project(url):
    project = db.projects.find_one({"href": url})
    if not project:
        data = request(url)
        convert_date(data, 'created', 'updated')
        # FIXME: This would be ideal, but Eve doesn't like it
        # data['_id'] = data.pop('id')
        return db.projects.insert(data)
    return project['_id']


def populate_organisation(url):
    organisation = db.organisations.find_one({"href": url})
    if not organisation:
        data = request(url)
        convert_date(data, 'created', 'updated')
        for address in data['addresses']['address']:
            convert_date(address, 'created', 'updated')
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


def populate_db(page=1, size=100, end=maxsize):

    def append_rel(rel, url, person):
        if not rel in person:
            person[rel] = []
        # FIXME: should be: person[rel].append(rel2func[rel](url))
        person[rel].append(rel2func[rel](url))

    def get_person(person):
        convert_date(person, 'created', 'updated')
        for link in person['links']['link']:
            try:
                append_rel(link['rel'], link['href'], person)
            except FailedRequest as e:
                debug("Request to %s failed: %s" % (link['href'], e.message))
        return person

    total = maxint
    while page <= min(end, total):
        payload = {'p': page, 's': size}
        data = request('http://gtr.rcuk.ac.uk/gtr/api/persons', payload)
        persons = [get_person(person) for person in data['person']]
        ids = db.persons.insert(persons)
        total = data['totalPages']
        debug("On page %d/%d, inserted persons %s" % (page, total, ids))
        page = data['page'] + 1

if __name__ == '__main__':
    getLogger().setLevel(DEBUG)
    populate_db()
