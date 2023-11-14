# Migrate from MongoDB to ElasticSearch

import datetime
import json

from elasticsearch import Elasticsearch, helpers
from pymongo import MongoClient


MONGO_DB_HOST = "176.57.213.53"
MONGO_DB_PORT = 27017
MONGO_DB_DATABASE = "pets"
MONGO_DB_USERNAME = "root"
MONGO_DB_PASSWORD = "toor"

ELASTICSEARCH_DB_HOST = "localhost"
ELASTICSEARCH_DB_PORT = 9200
MELASTICSEARCH_DB_DATABASE = "pets"
ELASTICSEARCH_DB_USERNAME = "root"
ELASTICSEARCH_DB_PASSWORD = "toor"

# Mongo Config
client = MongoClient(f"mongodb://{MONGO_DB_HOST}:{MONGO_DB_PORT}")
db = client[MONGO_DB_DATABASE]
collection = db[MONGO_DB_DATABASE]

# Elasticsearch Config
es = Elasticsearch([f"http://{ELASTICSEARCH_DB_HOST}:{ELASTICSEARCH_DB_PORT}/"])
es_index = MELASTICSEARCH_DB_DATABASE


def defaultconverter(o):
    if isinstance(o, datetime):
        return o.__str__()


def migrate():
    res = collection.find()
    # number of docs to migrate
    num_docs = 2000
    actions = []
    for i in range(num_docs):
        doc = res[i]
        mongo_id = doc['_id']
        doc.pop('_id', None)
        actions.append({
            "_index": es_index,
            "_id": mongo_id,
            "_source": json.dumps(doc, default = defaultconverter)
        })
    helpers.bulk(es, actions)

migrate()