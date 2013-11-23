from datetime import datetime
from sys import maxint

import requests


def request(url, params=None, headers=None):
    r = requests.get(url, params=params, headers=headers)
    if not r.status_code == 200:
        raise RuntimeError(r.json())
    return r.json()


def get_project(url):
    return request(url)


def get_organisation(url):
    return request(url)


rel2func = {
    'PI_PER': get_project,
    'COI_PER': get_project,
    'FELLOW_PER': get_project,
    'EMPLOYED': get_organisation
}


def populate_db(page=1, size=100, end=maxint):

    def append_rel(rel, url, person):
        if not rel in person:
            person[rel] = []
        # FIXME: should be: person[rel].append(rel2func[rel](url))
        data = request(url)
        # Remove the links since we're not following them for now
        data.pop('links', None)
        person[rel].append(data)

    total = 1
    while page <= min(end, total):
        payload = {'p': page, 's': size}
        data = request('http://gtr.rcuk.ac.uk/gtr/api/persons.json', payload)
        for person in data['person']:
            person['created'] = datetime.fromtimestamp(person['created']/1000)
            for link in person['links']['link']:
                append_rel(link['rel'], link['href'] + '.json', person)
        page = data['page'] + 1
        total = data['totalPages']

if __name__ == '__main__':
    populate_db(size=10, end=1)
