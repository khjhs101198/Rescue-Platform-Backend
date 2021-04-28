from flask import Flask
from flask_mqtt import Mqtt
import json
app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = '140.116.245.233'
# app.config['MQTT_BROKER_PORT'] = 3001
app.config['MQTT_USERNAME'] = 'admin'
app.config['MQTT_PASSWORD'] = 'admin'
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)
@app.route('/')
def index():
    return 'hello world'

@app.route('/api/v1.0/mqtt/pub/<want_to_pub>', methods=['GET'])
def pub_my_msg(want_to_pub):
    if len(want_to_pub) == 0:
        abort(404)
    mqtt.publish('mytopic',want_to_pub )
    return want_to_pub

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('GIOT-GW/UL/80029CF7BD76')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    payload = message.payload.decode()
    p = json.loads(payload)
    print("-------msg-------")
    print(p)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3001)