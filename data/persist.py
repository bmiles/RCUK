from sqlalchemy import create_engine,String,Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import requests
import json

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    PersonID = Column(String(255),primary_key=True)


if __name__ == '__main__':
    engine = create_engine('mysql://rcuk:rcuk1234@172.16.97.5/gtr_repo',echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    persons = [p for p, in session.query(Person.PersonID).all()]

    for person_id in persons:
        r = requests.get('http://gtr.rcuk.ac.uk:80/gtr/api/persons/{id}.json'.format(id=person_id))
        o = json.loads(r.text)
        for link in o.get('links',{}).get('link',[]):
            l = link['href']
            if 'projects' in l:
                p = requests.get(l + '.json')
                details = json.loads(p.text)
                print details.get('title',''),details.get('abstractText','')
