from sqlalchemy import create_engine,String,Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import requests

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'    
    PersonID = Column(String(255),primary_key=True)


engine = create_engine('mysql://rcuk:rcuk1234@172.16.97.5/gtr_repo',echo=False)
Session = sessionmaker(bind=engine)
session = Session()

persons = [p for p, in session.query(Person.PersonID).all()]

for person_id in persons:
    r = requests.get('http://gtr.rcuk.ac.uk:80/gtr/api/persons/{id}'.format(id=person_id))
