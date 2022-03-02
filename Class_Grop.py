from flask import Flask, render_template, jsonify, request ,flash,redirect, url_for
from flask_mqtt import Mqtt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_apscheduler import APScheduler
import json
import importlib
import sys
importlib.reload(sys)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://Tsen:CTsen@localhost/smartdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app1 = Flask(__name__)
app1.config['MQTT_BROKER_URL'] = '140.116.245.233'
# app.config['MQTT_BROKER_PORT'] = 3001
app1.config['MQTT_USERNAME'] = 'admin'
app1.config['MQTT_PASSWORD'] = 'admin'
app1.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds

db = SQLAlchemy(app)
CORS(app)
mqtt = Mqtt(app1)

@app.after_request
def add_headers(response):
    response.headers.add('Content-Type', 'application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Content-Length,Authorization,X-Pagination')
    return response
# Mqtt 
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('GIOT-GW/UL/80029CF7BD76')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    payload = message.payload.decode()
    p = json.loads(payload)
    d = {}
    d = dict(p[0])
    print("-------msg-------")
    print("Mac address :",d['macAddr'])
    print("Data :",d['data'])
    

class seeds(db.Model):  
    seed_id = db.Column(db.Integer , primary_key=True, nullable=False)
    seed_x = db.Column(db.Float)
    seed_y = db.Column(db.Float)
    seed_z = db.Column(db.Float)
    seed_battery = db.Column(db.Float)
    seed_status = db.Column(db.Integer)
    seed_latitude = db.Column(db.Float, nullable=False)
    seed_longitude = db.Column(db.Float, nullable=False)
    seed_admin = db.Column(db.VARCHAR(10))
    def __init__(self, seed_id, seed_x, seed_y, seed_z, seed_battery, seed_status, seed_latitude, seed_longitude, seed_admin):
        self.seed_id = seed_id
        self.seed_x = seed_x
        self.seed_y = seed_y
        self.seed_z = seed_z
        self.seed_battery = seed_battery
        self.seed_status = seed_status
        self.seed_latitude = seed_latitude
        self.seed_longitude = seed_longitude
        self.seed_admin = seed_admin
        

class firestation(db.Model):  
    team_name = db.Column(db.String, primary_key=True, nullable=False)
    brigade = db.Column(db.String, nullable=False)
    squadron  = db.Column(db.String, nullable=False)
    area_code = db.Column(db.CHAR(50))
    address = db.Column(db.VARCHAR(500))
    phone_number = db.Column(db.CHAR(50))
    dax_number = db.Column(db.CHAR(50))
    fireStation_latitude = db.Column(db.Float, nullable=False)
    fireStation_longitude = db.Column(db.Float, nullable=False)
    def __init__(self, team_name, brigade,squadron,area_code,address,phone_number,dax_number,fireStation_latitude,fireStation_longitude):
        self.team_name =  team_name
        self.brigade =  brigade
        self.squadron = squadron
        self.area_code = area_code
        self.address = address
        self.phone_number = phone_number
        self.dax_number = dax_number
        self.fireStation_latitude = fireStation_latitude
        self.fireStation_longitude = fireStation_longitude

class firestation_car(db.Model):  
    car_license_plate = db.Column(db.CHAR(50), primary_key=True, nullable=False)
    team_name = db.Column(db.CHAR(50), nullable=False)
    car_latitude  = db.Column(db.Float, nullable=False)
    car_longitude = db.Column(db.Float, nullable=False)
    car_status = db.Column(db.Integer)
    car_kind = db.Column(db.Integer)
    car_where = db.Column(db.VARCHAR(100), nullable=False)

    def __init__(self, car_license_plate, team_name, car_latitude,car_longitude, car_status, car_kind, car_where):
        self.car_license_plate =  car_license_plate
        self.team_name =  team_name
        self.car_latitude = car_latitude
        self.car_longitude = car_longitude
        self.car_status = car_status
        self.car_kind = car_kind
        self.car_where = car_where

class volunteers(db.Model):  
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    have_task = db.Column(db.Integer)
    latitude  = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    state = db.Column(db.Integer)

    def __init__(self, id, have_task, latitude,longitude, state):
        self.id =  id
        self.have_task =  have_task
        self.latitude = latitude
        self.longitude = longitude
        self.state = state

class light_pole(db.Model):  
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    token = db.Column(db.CHAR(10),nullable=False)
    time_phase  = db.Column(db.Integer)

    def __init__(self, id, token, time_phase):
        self.id =  id
        self.token = token
        self.time_phase = time_phase

class task_package(db.Model):  
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    task_date = db.Column(db.Date)
    latitude  = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    taskinfo = db.Column(db.VARCHAR(500))

    def __init__(self, id, task_date, latitude,longitude, taskinfo):
        self.id =  id
        self.task_date =  task_date
        self.latitude = latitude
        self.longitude = longitude
        self.taskinfo = taskinfo