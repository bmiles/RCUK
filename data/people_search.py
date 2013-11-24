from os import environ
from sys import maxint
from logging import getLogger, DEBUG, debug

from pymongo import MongoClient
import requests

import csv
import json

api_stem = "http://gtr.rcuk.ac.uk/gtr/api/"

def search(topic):
    dbname = environ['MONGOLAB_URI'].rsplit('/', 1)[1]
    db = MongoClient(environ['MONGOLAB_URI'])[dbname]

    project_persons = read_json_file('person_projects.json')
    person_score = read_csv_file('person_score.csv')

    projects_json = request(api_stem + "projects", {'q': 'pro.a={topic}'.format(topic=topic), 's': 100})

    persons = []
    for project in projects_json.get('project', []):
        for link in project.get('links', {}).get('link', []):
            if "person" in link.get('href', ''):
                persons.append(link.get('href').split('/')[-1])

    persons = set(persons)
    sorted_persons = sorted(persons, key=lambda person: -person_score[person])

    result = dict([(person,person_score.get(person,0)) for person in sorted_persons])
    return result


def request(url, params=None, headers=None):
    debug("Querying %s.json with params %r and headers %r" % (url, params, headers))
    r = requests.get(url + '.json', params=params, headers=headers)
    if not r.status_code == 200:
        raise FailedRequest(r.json())
    return r.json()

def read_json_file(filename):
    with open(filename, 'rb') as f:
        return json.load(f)

# 1: NumOrgs
# 2: NumPrivateOrgs
# 3: NumProjects
# 4: TotalMoney
# 5: PrivateMoney
def read_csv_file(filename):
    content = {}
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'PersonId':
                content[row[0]] = float(row[2])

    return content
