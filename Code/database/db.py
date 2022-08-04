from http import client
import pymongo

class Database():
    mongodb_uri = 'mongodb+srv://msi:msi_password_22@notesdb.emrguqn.mongodb.net/?retryWrites=true&w=majority'
    DATABASE = None

    @staticmethod
    def Initialize():
        client = pymongo.MongoClient(Database.mongodb_uri)
        Database.DATABASE = client['notesdb']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)