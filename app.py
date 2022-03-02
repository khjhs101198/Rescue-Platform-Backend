from Class_Grop import *
from SQL_data_preprocess.SQL_Table.Datetime_To import *
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
            NewSeed = seeds(item['seed_id'],0,0,0,100,item['seed_status'],item['seed_latitude'],item['seed_longitude'],item['seed_admin'])
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
                # 'seed_latitude' : item['seed_latitude'] ,
                # 'seed_longitude' : item['seed_longitude'] , 
                'seed_battery' : item['seed_battery'] , 
                'seed_status' :item['seed_status']})
        else :
            return "Seed does not exist." 
    db.session.commit()
    return json.dumps(request_json,ensure_ascii=False)        

# All information of cars will send to this route.
@app.route('/GetCarsJson', methods=['GET','POST'])
def ReturnCarsJson():
    List = []
    i = 0
    carall = firestation_car.query.all()
    for car in carall:
        List.append({'car_license_plate':car.car_license_plate,
        'team_name':car.team_name,
        'car_latitude':car.car_latitude,
        'car_longitude':car.car_longitude,
        'car_status':car.car_status,
        'car_kind':car.car_kind,
        'car_where':car.car_where,
        })
        jsonData = json.dumps(List,ensure_ascii=False)
    return jsonData

# All information of cars will send to this route.
@app.route('/GetFireStationJson', methods=['GET','POST'])
def ReturnFireStationJson():
    List = []
    i = 0
    stationall = firestation.query.all()
    for station in stationall:
        List.append({'team_name':station.team_name,
        'brigade':station.brigade,
        'squadron':station.squadron,
        'area_code':station.area_code,
        'address':station.address,
        'phone_number':station.phone_number,
        'dax_number':station.dax_number,
        'fireStation_latitude':station.fireStation_latitude,
        'fireStation_longitude':station.fireStation_longitude
        })
        jsonData = json.dumps(List,ensure_ascii=False)
    return jsonData

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
        TheCar = firestation_car.query.filter_by(car_license_plate = item['car_license_plate']).first()
        if TheCar :
            firestation_car.query.filter_by(car_license_plate = item['car_license_plate'] ).update({'car_status' :item['car_status']})
        else :
            return "Car does not exist."
    db.session.commit()
    return json.dumps(request_carstatus_json,ensure_ascii=False)        

# Front-end send json to back-end to change car latitude and longitude.
@app.route('/ChangeCarItude', methods=['GET','POST'])
def ChangeCarItude():
    request_carstatus_json =request.get_json()
    print(request_carstatus_json)

    for item in request_carstatus_json:
    # Filter database, to find the car.
        TheCar = firestation_car.query.filter_by(car_license_plate = item['car_license_plate']).first()
        if TheCar :
            firestation_car.query.filter_by(car_license_plate = item['car_license_plate'] ).update({
                'car_latitude' :item['car_latitude'],
                'car_longitude' :item['car_longitude']
            })
        else :
            return "Car does not exist."
    db.session.commit()        
    return json.dumps(request_carstatus_json,ensure_ascii=False)

# Front-end send json to back-end to change car address.
@app.route('/ChangeCarAddress', methods=['GET','POST','OPTIONS'])
@cross_origin()
def ChangeCarAddress():
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
        TheCar = firestation_car.query.filter_by(car_license_plate = item['car_license_plate']).first()
        if TheCar :
            firestation_car.query.filter_by(car_license_plate = item['car_license_plate'] ).update({'car_where' :item['car_where']})
        else :
            return "Car does not exist."
    db.session.commit()
    return json.dumps(request_carstatus_json,ensure_ascii=False)        

@app.route('/GetVolunteersJson', methods=['GET','POST'])
def ReturnVolunteersJson():
    List = []

    volunteersall = volunteers.query.all()
    for volunteer in volunteersall:
        List.append({'id':volunteer.id,
        'have_task':volunteer.have_task,
        'state':volunteer.state,
        'latitude':volunteer.latitude,
        'longitude':volunteer.longitude
        })
        jsonData = json.dumps(List,ensure_ascii=False)
    return jsonData

@app.route('/GetTaskpackageJson', methods=['GET','POST'])
def ReturnTaskpackageJson():
    List = []

    task_packagesall = task_package.query.all()
    for package in task_packagesall:
        task_package.query.filter_by( id = package.id ).update({
            'task_date' : GetStrDate()
            }) 
    db.session.commit()

    for package in task_packagesall:
        List.append({'id':package.id,
        'taskinfo':package.taskinfo,
        'task_date':str(package.task_date),
        'latitude':package.latitude,
        'longitude':package.longitude
        })
        jsonData = json.dumps(List,ensure_ascii=False)
    return jsonData

@app.route('/GetLightpoleJson', methods=['GET','POST'])
def ReturnLightpoleJson():
    List = []
    light_polesall = light_pole.query.all()
    for pole in light_polesall:
        light_pole.query.filter_by( id = pole.id ).update({
            'token' : UpdateToken(pole.id)
            }) 
    db.session.commit()

    for pole in light_polesall:
        List.append({'id':pole.id,
        'token':pole.token,
        'time_phase':pole.time_phase
        })
        jsonData = json.dumps(List,ensure_ascii=False)
    return jsonData

@app.route('/GetTunnelKML', methods = ['GET','POST'])
def GetTunnelKML():
    f = open("中寮隧道.kml","task_package")
    kmll = f.read()
    return kmll

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3000)