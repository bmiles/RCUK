import csv
import json

from eve.methods.get import getitem

from gtr import request


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

api_stem = "http://gtr.rcuk.ac.uk/gtr/api/"
person_score = read_csv_file('data/person_score.csv')


def search(topic):
    def get_person(pid):
        # We're only interested in the actual person object
        person, _, _, _ = getitem('persons', id=pid)
        person['score'] = person_score.get(pid, 0.0)
        return person
    projects_json = request(api_stem + "projects",
                            {'q': 'pro.a=%s' % topic, 's': 100})

    persons = []
    for project in projects_json.get('project', []):
        for link in project.get('links', {}).get('link', []):
            if "person" in link.get('href', ''):
                persons.append(link.get('href').split('/')[-1])

    persons = sorted(set(persons), key=lambda person: -person_score[person])
    return [get_person(pid) for pid in persons]


def read_json_file(filename):
    with open(filename, 'rb') as f:
        return json.load(f)
