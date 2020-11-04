# Import the python libraries
from dbconfig import DBConfig
from bson.json_util import dumps

class DB_DAO:

   # configuration of the database
   def __init__(self):
      self.db = DBConfig()

   # get the collection of cars as JSON
   def get_cars(self):
      documents = self.db.find_collection("cars")
      json_data = dumps(documents)
      return json_data

   # get the collection of customers as JSON
   def get_customers(self):
      documents = self.db.find_collection("customers")
      json_data = dumps(documents)
      return json_data

   # get the collection of bookings as JSON
   def get_bookings(self):
      return self.db.find_collection("bookings")

   # import multiple documents into a specific collection
   def import_data(self, collection,json_data):
      if self.db.find_collection(collection).count() == 0:
         self.db.insert_many_data(collection, json_data)
         print("Data has been imported")
      else:
         print("Data already existing. Import has been canceled.")

   # import one document into a specific collection
   def insert_data(self, collection,json_data):
      return self.db.insert_only_one_data(collection, json_data)
