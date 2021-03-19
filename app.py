from flask import Flask, render_template, jsonify, request
from flask import flash,redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_apscheduler import APScheduler
import requests
import json
import importlib
import sys
importlib.reload(sys)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://Tsen:CTsen@localhost/smartdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)

@app.after_request
def add_headers(response):
    response.headers.add('Content-Type', 'application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Content-Length,Authorization,X-Pagination')
    return response


class seeds(db.Model):  
    seed_id = db.Column(db.Integer , primary_key=True)
    seed_x = db.Column(db.Float)
    seed_y = db.Column(db.Float)
    seed_z = db.Column(db.Float)
    seed_battery = db.Column(db.Float)
    seed_status = db.Column(db.Integer)
    seed_latitude = db.Column(db.Float)
    seed_longitude = db.Column(db.Float)

    def __init__(self, seed_id, seed_x, seed_y, seed_z, seed_battery, seed_status, seed_latitude, seed_longitude):
        self.seed_id = seed_id
        self.seed_x = seed_x
        self.seed_y = seed_y
        self.seed_z = seed_z
        self.seed_battery = seed_battery
        self.seed_status = seed_status
        self.seed_latitude = seed_latitude
        self.seed_longitude = seed_longitude

class cars(db.Model):  
    car_license_plate = db.Column(db.String, primary_key=True)
    car_latitude  = db.Column(db.Float)
    car_longitude = db.Column(db.Float)
    car_status = db.Column(db.Integer)

    def __init__(self,car_license_plate,car_latitude,car_longitude,car_status):
        self.car_license_plate =  car_license_plate
        self.car_status = car_status
        self.car_latitude = car_latitude
        self.car_longitude = car_longitude


@app.route('/')
def index():
    return "Hello Word!"

# All information of seeds will send to this route.
@app.route('/GetSeedsJson', methods=['GET','POST'])
def ReturnSeedsJson():
    List = []
    i = 0
    seedall = seeds.query.all()
    for seed in seedall:
        List.append({'seed_id':seed.seed_id,
        'seed_x':seed.seed_x,
        'seed_y':seed.seed_y,
        'seed_z':seed.seed_z,
        'seed_latitude':seed.seed_latitude,
        'seed_longitude':seed.seed_longitude,
        'seed_battery':seed.seed_battery,
        'seed_status':seed.seed_status,

        })
        jsonData = json.dumps(List)
    return jsonData

# Front-end send json to back-end to register seed.
register_seed_json = ''
@app.route('/RegisterSeeds', methods=['GET','POST'])
@cross_origin()
def RegisterSeeds():
    # get want update data
    global register_seed_json 
    register_seed_json = request.json
    print(register_seed_json)
    # print json data
    for item in register_seed_json:
        TheSeed = seeds.query.filter_by( seed_id = item['seed_id'] ).first()
        # If the corresponding seedID is not found, a new one will be created , else update.
        if TheSeed :
            return "The seed has already been registered."
        else :
            NewSeed = seeds(item['seed_id'],0,0,0,100,item['seed_status'],item['seed_latitude'],item['seed_longitude'])
            db.session.add(NewSeed)
            db.session.commit()
            return json.dumps(request_json,ensure_ascii=False) 

# Front end wanna update information of seeds, it will send json flie to this route. 
request_json = ''
@app.route('/UpdateSeeds', methods=['GET','POST','OPTIONS'])
def UpdateSeeds():
    global request_json
    request_json = request.json
    # Item will track json array.
    for item in request_json:

        TheSeed = seeds.query.filter_by( seed_id = item['seed_id'] ).first()
        # If the corresponding seedID is not found, a new one will be created , else update.
        if TheSeed :
            seeds.query.filter_by( seed_id = item['seed_id'] ).update({
                'seed_x' : item['seed_x'] , 
                'seed_y' : item['seed_y'] , 
                'seed_z' : item['seed_z'] ,
                'seed_latitude' : item['seed_latitude'] ,
                'seed_longitude' : item['seed_longitude'] , 
                'seed_battery' : item['seed_battery'] , 
                'seed_status' :item['seed_status']})
            db.session.commit()
            return json.dumps(request_json,ensure_ascii=False) 

        else :
            return "Seed does not exist." 

# All information of cars will send to this route.
@app.route('/GetCarsJson', methods=['GET','POST'])
def ReturnCarsJson():
    List = []
    i = 0
    carall = cars.query.all()
    for car in carall:
        List.append({'car_license_plate':car.car_license_plate,
        'car_latitude':car.car_latitude,
        'car_longitude':car.car_longitude,
        'car_status':car.car_status
        })
        jsonData = json.dumps(List)
    return jsonData

# All information of cars will send to this route.
@app.route('/GetFireStationJson', methods=['GET','POST'])
def ReturnFireStationJson():
    users = {}
    with open('output-merge.json', 'r') as f:
          jsonData = f.read()
    return  jsonData

# Front-end send json to back-end to change car status.
@app.route('/ChangeCarStatus', methods=['GET','POST','OPTIONS'])
@cross_origin()
def ChangeCarStatus():
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
            'Access-Control-Max-Age': 1000,
            'Access-Control-Allow-Headers':'Authorization, Content-Type',
            'Access-Control-Allow-Headers': 'origin, x-csrftoken, content-type accept',
        }
        return '', 200, headers

    request_carstatus_json =request.get_json(force=True)
    print(request_carstatus_json)

    for item in request_carstatus_json:
    # Filter database, to find the car.
        TheCar = cars.query.filter_by(car_license_plate = item['car_license_plate']).first()
        if TheCar :
            cars.query.filter_by(car_license_plate = item['car_license_plate'] ).update({'car_status' :item['car_status']})
            db.session.commit()
            return json.dumps(request_carstatus_json,ensure_ascii=False)
        else :
            return "Car does not exist."


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3000)