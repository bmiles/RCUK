"""Global API configuration."""

from os import environ
from urllib.parse import urlparse

from schemas import organisation_schema, person_schema, project_schema

API_NAME = 'ResearchConnect'
URL_PREFIX = 'api'
if 'EVE_DEBUG' in environ:
    DEBUG = True

if 'MONGOLAB_URI' in environ:
    url = urlparse(environ['MONGOLAB_URI'])
    MONGO_HOST = url.hostname
    MONGO_PORT = url.port
    MONGO_USERNAME = url.username
    MONGO_PASSWORD = url.password
    MONGO_DBNAME = url.path[1:]
else:
    MONGO_DBNAME = API_NAME

organisations = {
    "item_title": "organisations",
    "schema": organisation_schema,
    "resource_methods": ['GET'],
}

persons = {
    "item_title": "persons",
    "schema": person_schema,
    "embedding": True,
    "embedded_fields": ["PI_PER", "COI_PER", "PM_PER", "FELLOW_PER", "EMPLOYEE"],
    "resource_methods": ['GET'],
}

projects = {
    "item_title": "projects",
    "schema": project_schema,
    "resource_methods": ['GET'],
}

DOMAIN = {
    'organisations': organisations,
    'persons': persons,
    'projects': projects,
}

# FIXME: Temporarily allow CORS requests for development purposes
X_DOMAINS = "*"
