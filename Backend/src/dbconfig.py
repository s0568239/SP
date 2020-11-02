from pymongo import MongoClient
from bson.json_util import dumps

class DBConfig:
    db = None
    client = None

    def __init__(self):
        #Starting working with MongoDB
        self.client = MongoClient('mongodb://htw-spezprog-database_c:27017/')
        self.db = self.client["rentMe"]

    def getFind(self, collection):
        col = self.db[collection]
        documents = col.find({})
        list_documents = list(documents)
        json_data = dumps(list_documents)
        return json_data

    def insertManyData(self, collection, json_data):
        collections = self.db[collection]
        collections.insert_many(json_data)

    def insertOnlyOneData(self, collection, json_data):
        collections = self.db[collection]
        collections.insert_one(json_data)
