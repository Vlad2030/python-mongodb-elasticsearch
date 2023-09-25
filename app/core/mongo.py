from mongoengine import connect

connection = connect(
    db="pets",
    name=None,
    host="192.168.1.65",
    port=27017,
    username="root",
    password="toor",
)