# Import notwendiger Bibliotheken / Abhängigkeiten / Module
from flask import Flask, jsonify, request
from Car_bookings import Car_bookings
from Cars import Cars
from Customer_manager import Customer_manager
import json

# Test-data aus den json-Files laden
cars_manager = Cars()
cars_manager.export_data()

with open('car_data.json') as json_car_data:
    car_data = json.load(json_car_data)

customer_manager = Customer_manager()
customer_manager.export_data()

with open('customer_data.json') as json_customer_data:
    customer_data = json.load(json_customer_data)

# Instanz eines Car-Booking-Manager erstellen        
booking_manager = Car_bookings(car_data, customer_data)

# Instanz eines Python-Webservers
app = Flask(__name__)

# Route hinzufügen, die aufrufbar ist unter /all_cars
@app.route('/all_cars')
def all_cars():
    return jsonify(booking_manager.cars), 200

# Route hinzufügen, die aufrufbar ist unter /customers
@app.route('/customers')
def all_customers():
    return jsonify(booking_manager.customers), 200

# Route hinzufügen, die aufrufbar ist unter /all_bookings
@app.route('/all_bookings')
def all_bookings():
    return jsonify(booking_manager.all_bookings()), 200

# Route hinzufügen, die aufrufbar ist unter /booking
@app.route('/booking', methods=['POST'])
def create_booking():
    customer_id = request.args.get('customer_id')
    car_id = request.args.get('car_id')
    begin = request.args.get('begin')
    end = request.args.get('end')
    return booking_manager.book(customer_id, car_id, begin, end), 201

# Route hinzufügen, die aufrufbar ist unter /unbooking
@app.route('/unbooking', methods=['POST'])
def create_unbooking():
    car_id = request.args.get('car_id')
    return booking_manager.unbook(car_id), 201

app.run(host='0.0.0.0', port=4000)