from Customer import Customer
import json

class Customer_manager(list):
    
    def __init__(self):
        customer_data = [
            {
                'customer_id': 1,
                'name': 'Frank Weider',
                'street': 'Weinmarstr.',
                'number': 46,
                'city': 'Berlin',
                'country': 'Germany',
                'zip': 12345,
                'age': 24
            },
            {
                'customer_id': 2,
                'name': 'Heinz Meiler',
                'street': 'Karl-Lange Str..',
                'number': 21,
                'city': 'Berlin',
                'country': 'Germany',
                'zip': 11002,
                'age': 35
            },
            {
                'customer_id': 3,
                'name': 'Thomas Mannheimer',
                'street': 'Grosse Allee',
                'number': 3,
                'city': 'Berlin',
                'country': 'Germany',
                'zip': 11309,
                'age': 30
            },
            {
                'customer_id': 4,
                'name': 'Anja Meier',
                'street': 'Gruene Ecke',
                'number': 90,
                'city': 'Berlin',
                'country': 'Germany',
                'zip': 10045,
                'age': 19
            },
            {
                'customer_id': 5,
                'name': 'Margaret Daimer',
                'street': 'Pfauenweg',
                'number': 14,
                'city': 'Berlin',
                'country': 'Germany',
                'zip': 10078,
                'age': 30
            }
        ]

        for i in customer_data:
            customer = Customer(i['customer_id'], i['name'], i['street'], i['number'], i['city'], i['zip'], i['country'], i['age'])
            self.append(customer)
        
    def find(self, customer_id):
        for i in self:
            if i.customer_id == customer_id:
                return i
            
    def export_data(self):
        a = list()
        with open('customer_data.json', 'w') as f:
            for i in range(len(self)):
                a.append(self[i].__dict__)
            json.dump(a, f)
            
                
t = Customer_manager()
t.export_data()