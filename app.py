from flask import Flask, render_template, jsonify, request
from flask import flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from random import randint
import sqlite3
import datetime,os
import requests 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users//tsen//Documents//Python//Flask//Edge_Seeds_Info//database1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Seed(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    seedID = db.Column(db.Integer ,unique = True)
    x = db.Column(db.Float)
    y = db.Column(db.Float)
    z = db.Column(db.Float)
    n = db.Column(db.Numeric(10, 7))
    e = db.Column(db.Numeric(10, 7))
    battery = db.Column(db.Integer)
    status = db.Column(db.Integer)

    def __init__(self, seedID, x, y, z, n, e, battery, status):
        self.seedID = seedID
        self.x = x
        self.y = y
        self.z = z
        self.n = n
        self.e = e
        self.battery = battery
        self.status = status

@app.route('/')
def index():
    seeds = Seed.query.all()
    return render_template('index.html', seeds=seeds)

# request json Flie 
request_json = ''
@app.route('/', methods=['POST'])
def request_json_flie():
    global request_json
    request_json = request.json
    # Item will track json array.
    for item in request_json:
        print("seedID:" + str(item['seedID']))
        print("x:" + str(item['x']))
        print("y:" + str(item['y']))
        print("z:" + str(item['z']))
        print("n:" + str(item['n']))
        print("e:" + str(item['e']))
        print("battery:" + str(item['battery']))
        print("status:" + str(item['status']))

        TheSeed = Seed.query.filter_by( seedID = item['seedID'] ).first()
        # If the corresponding seedID is not found, a new one will be created , else update.
        if TheSeed :
            Seed.query.filter_by( seedID = item['seedID'] ).update({
                'x' : item['x'] , 
                'y' : item['y'] , 
                'z' : item['z'] , 
                'battery' : item['battery'] , 
                'status' :item['status']})
            db.session.commit()

        else :
            NewSeed = Seed(item['seedID'], item['x'], item['y'], item['z'], item['n'], item['e'], item['battery'], item['status'])
            db.session.add(NewSeed)
            db.session.commit()

    return json.dumps(request_json,ensure_ascii=False)    

@app.route('/update')
def update():
    seeds = Seed.query.all()
    #return jsonify({'result' : 'success', 'member_num' : member.random})
    return render_template('section.html', seeds=seeds)  


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=2000)