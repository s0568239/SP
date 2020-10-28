from Booking import Booking

import time
import datetime
get_datetime = lambda date_time_str: datetime.datetime.strptime(date_time_str, '%d.%m.%Y %H:%M:%S')
import json

class Car_bookings(list):
    def __init__(self, cars, customers):
        self.cars = cars
        self.customers = customers
        self.counter = 0

        booking_data = [
        {
            'customer_id': 1,
            'car_id': 'B HF 6903',
            'begin': '20.10.2020 12:00:00',
            'end': '22.10.2020 12:00:00',
        },
        {
            'customer_id': 4,
            'car_id': 'B ENG 5689',
            'begin': '12.10.2020 09:00:00',
            'end': '16.10.2020 18:00:00',
        }]
        
        for i in booking_data:
            self.counter += 1
            booking = Booking(self.counter, i['customer_id'], i['car_id'], i['begin'], i['end'])
            self.append(booking)
        
    def book(self, customer_id, car_id, begin, end):
        car = {}
        customer = {}
        for i in range(len(self.cars)):
            if self.cars[i]['car_id'] == car_id:
                car = self.cars[i]
                    
        for i in range(len(self.customers)):
            if self.customers[i]['customer_id'] == customer_id:
                customer = self.customers[i]
                           
        if (car['status'] == 'available' and customer != ""):
            booking = Booking(self.counter, customer_id, car, begin, end)
            self.counter = self.counter+1
            for i in range(len(self.cars)):
                if self.cars[i]['car_id'] == car_id:
                    self.cars[i]['status'] = 'booked'
            self.append(booking)
            return('Booked for {}, car is no longer available from {} to {} with the booking-Id: {}'.format(car_id, begin, end, self.counter))
        elif customer == "":
            return "Customer doesn't exist"   
        else:
            return(car['car_id'] + " isn't available")
            
    def unbook(self, car_id):
        for i in range(len(self.cars)):
            if self.cars[i]['car_id'] == car_id:
                self.cars[i]['status'] = 'available'
        return('Car {} has been unbooked and is available again'.format(car_id))

    def all_bookings(self):
        self.list = []
        for i in self:
            self.list.append(i.__dict__)
        return self.list


 

