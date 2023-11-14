import random
from datetime import datetime

from loguru import logger

ELASTICSEARCH_DB_HOST = "192.168.1.65"
ELASTICSEARCH_DB_PORT = 9200
MELASTICSEARCH_DB_DATABASE = "pets"
ELASTICSEARCH_DB_USERNAME = "root"
ELASTICSEARCH_DB_PASSWORD = "toor"

PETS_AMOUNT = 50


# class Pets(Document):
#     name = StringField(min_length=1, max_length=256)
#     age = IntField(min_value=1, max_value=256)
#     created_at = DateTimeField(default=datetime.now)


if __name__ == "__main__":
    logger.info("MongoDB connecting")
