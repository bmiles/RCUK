from os import environ
from sys import maxint
from logging import getLogger, DEBUG, debug

from pymongo import MongoClient
import requests

import csv
import json

dbname = environ['MONGOLAB_URI'].rsplit('/', 1)[1]
db = MongoClient(environ['MONGOLAB_URI'])[dbname]

with open('person_projects.json', 'rb') as f:
    person_projects = json.load(f)

# 1: NumOrgs
# 2: NumPrivateOrgs
# 3: NumProjects
# 4: TotalMoney
# 5: PrivateMoney
person_score = {}
with open('person_score.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] != 'PersonId':
            person_score[row[0]] = float(row[2])

def request(url, params=None, headers=None):
    debug("Querying %s.json with params %r and headers %r" %
          (url, params, headers))
    r = requests.get(url + '.json', params=params, headers=headers)
    if not r.status_code == 200:
        raise FailedRequest(r.json())
    return r.json()

api_stem = "http://gtr.rcuk.ac.uk/gtr/api/"

projects_json = request(api_stem + "projects", {'q': 'pro.a=physics', 's': 100})

persons = []
for project in projects_json.get('project', []):
    for link in project.get('links', {}).get('link', []):
        if "person" in link.get('href', ''):
            persons.append(link.get('href').split('/')[-1])

persons = set(persons)
sorted_persons = sorted(persons, key=lambda person: -person_score[person])

print "\n".join([str((person, person_score[person])) for person in sorted_persons])
