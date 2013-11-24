import csv
import json
import requests
import urllib
from gtr import request, db

from eve.methods.get import getitem

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
                content[row[0]] = {
                    'NumOrgs' : int(row[1]),
                    'NumPrivateOrgs' : float(row[2]),
                    'NumProject' : int(row[3]),
                    'TotalMoney' : float(row[4]),
                    'PrivateMoney' : float(row[5])
                    }

    return content



api_stem = "http://gtr.rcuk.ac.uk/gtr/api/"
person_score = read_csv_file('../data/person_score.csv')


def search(topic):
    def get_person(pid):
        # We're only interested in the actual person object
        person, _, _, _ = getitem('persons', id=pid)
        scores = person_score.get(pid,{})
        person['score'] = scores.get('NumPrivateOrgs',0.0)
        person['num_orgs'] = scores.get('NumOrgs',0)
        person['num_projects'] = scores.get('NumProject',0)
        person['total_money'] = scores.get('TotalMoney',0.0)
        person['private_money'] = scores.get('PrivateMoney',0.0)
        return person

    projects_json = request(api_stem + "projects",
                            {'q': 'pro.a=%s' % urllib.quote_plus(topic),
                             's': 100})

    persons = []
    for project in projects_json.get('project', []):
        for link in project.get('links', {}).get('link', []):
            if "person" in link.get('href', ''):
                persons.append(link.get('href').split('/')[-1])

    persons = sorted(set(persons), key=lambda person: -person_score.get(person,{}).get('NumPrivateOrgs',0))
    return [get_person(pid) for pid in persons]


def read_json_file(filename):
    with open(filename, 'rb') as f:
        return json.load(f)


def search_in_orcid(name):
    names = name.split()
    s = requests.Session()
    s.headers.update({'Accept':'application/orcid+json'})
    r = s.get('http://pub.orcid.org/search/orcid-bio?q=family-name:{surname}+AND+given-names:{firstname}&start=0&rows=1'.format(surname=names[-1],firstname=' '.join(urllib.quote_plus(' '.join([names[x] for x in range(0,len(names)-1)])))))

    return json.loads(r.text).get('orcid-search-results',{}).get('orcid-search-result',[{'orcid-profile':'None'}])[0]
