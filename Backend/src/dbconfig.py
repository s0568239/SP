# Import the python libraries
from pymongo import MongoClient

class DBConfig:

    def __init__(self):
        # Choose the appropriate client
        self.client = MongoClient('mongodb://htw-spezprog-database_c:27017/')
        # Connect to the test db 
        self.db = self.client["rentMe"]

    # find specific collection
    def find_collection(self, collection):
        return self.db[collection].find()

    # insert many documents in specific collection
    def insert_many_data(self, collection, json_data):
        collections = self.db[collection]
        collections.insert_many(json_data)

    # insert one documents in specific collection
    def insert_only_one_data(self, collection, json_data):
        collections = self.db[collection]
        collections.insert_one(json_data)
