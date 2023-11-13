from datetime import datetime
import random
from mongoengine import connect
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, IntField, StringField
from loguru import logger


MONGO_DB_HOST = "172.21.0.2"
MONGO_DB_PORT = 27017
MONGO_DB_DATABASE = "pets"
MONGO_DB_USERNAME = "root"
MONGO_DB_PASSWORD = "toor"

ELASTICSEARCH_DB_HOST = "192.168.1.65"
ELASTICSEARCH_DB_PORT = 9200
MELASTICSEARCH_DB_DATABASE = "pets"
ELASTICSEARCH_DB_USERNAME = "root"
ELASTICSEARCH_DB_PASSWORD = "toor"

PETS_AMOUNT = 50


class Pets(Document):
    name = StringField(min_length=1, max_length=256)
    age = IntField(min_value=1, max_value=256)
    created_at = DateTimeField(default=datetime.now)


if __name__ == "__main__":
    logger.info("MongoDB connecting")

    connection = connect(
        host=MONGO_DB_HOST,
        port=MONGO_DB_PORT,
        db=MONGO_DB_DATABASE,
        username=MONGO_DB_USERNAME,
        password=MONGO_DB_PASSWORD,
    )

    logger.success("MongoDB connected!")

    logger.info("Creating {amount} pets in MongoDB", amount=PETS_AMOUNT)

    for count, pet in enumerate(range(PETS_AMOUNT), start=1):
        _name = f"Pet{count}"
        _age = random.randint(1, 15)
        Pets(name=_name, age=_age).save()
        logger.info("{count}. {name} created", count=count, name=_name)

    logger.success("{amount} pets in MongoDB created!", amount=PETS_AMOUNT)


