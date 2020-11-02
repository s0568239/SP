from dbconfig import DBConfig

class DB_DAO:
    db = None

    def __init__(self):
       self.db = DBConfig()

    def getCars(self):
       return self.db.getFind("cars")

    def getCustomers(self):
       return self.db.getFind("customers")

    def getBookings(self):
       return self.db.getFind("bookings")

    def import_Data(self, collection,json_data):
       return self.db.insertManyData(collection, json_data)

    def insert_data(self, collection,json_data):
       return self.db.insertOnlyOneData(collection, json_data)
