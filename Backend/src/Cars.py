from Car import Car
import json

class Cars(list):
    
    def __init__(self):
        car_data = [
            {
                'car_id': 'B AB 4067',
                'brand': 'VW',
                'name': 'Golf 5',
                'seats': 4,
                'color': 'black',
                'price': 0.50,
                'status': 'available'
            },
            {
                'car_id': 'B RAS 667',
                'brand': 'Audi',
                'name': 'A5',
                'seats': 4,
                'color': 'grey',
                'price': 0.70,
                'status': 'available'
            },
            {
                'car_id': 'B ENG 5689',
                'brand': 'VW',
                'name': 'Passat',
                'seats': 4,
                'color': 'blue',
                'price': 0.65,
                'status': 'available'
            },
            {
                'car_id': 'B HF 6903',
                'brand': 'Renault',
                'name': 'Zoe',
                'seats': 4,
                'color': 'white',
                'price': 0.40,
                'status': 'available'
            },
            {
                'car_id': 'B RF 490',
                'brand': 'Mazda',
                'name': '3',
                'seats': 4,
                'color': 'red',
                'price': 0.50,
                'status': 'available'
            }
        ]

        for i in car_data:
            car = Car()
            car.car_id = i['car_id']
            car.brand = i['brand']
            car.name = i['name']
            car.seats = i['seats']
            car.color = i['color']
            car.price = i['price']
            car.status = i['status']
            self.append(car)
    
    def add(self, car_id, brand, name, seats, color, price, status):
        car = Car()
        car.car_id = car_id
        car.brand = brand
        car.name = name
        car.seats = seats
        car.color = color
        car.price = price
        car.status = status
        self.append(car)
            
    def export_data(self):
        a = list()
        with open('car_data.json', 'w') as f:
            for i in range(len(self)):
                a.append(self[i].__dict__)
            json.dump(a, f)
                
        
t = Cars()
t.export_data()
