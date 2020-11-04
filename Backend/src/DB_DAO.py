from dbconfig import DBConfig
from bson.json_util import dumps

class DB_DAO:
    #db = None

    def __init__(self):
       self.db = DBConfig()

    def getCars(self):
       documents = self.db.getFind("cars")
       json_data = dumps(documents)
       return json_data

    def getCustomers(self):
       documents = self.db.getFind("customers")
       json_data = dumps(documents)
       return json_data

    def getBookings(self):
       return self.db.getFind("bookings")

    def import_Data(self, collection,json_data):
      
       if self.db.getFind(collection).count() == 0:
          self.db.insertManyData(collection, json_data)
          print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
          print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
          print("Daten wurden importiert")
          print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
          print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
       else:
          print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
          print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
          print("Daten existieren bereit. Import wurde Übersprungen.")
          print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
          print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
      

    def insert_data(self, collection,json_data):
       return self.db.insertOnlyOneData(collection, json_data)
