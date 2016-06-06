from __init__ import *
from iAS.core.appmgt import appDAO
from random import randint
from iAS.core.devicemgt.DeviceDAO import *

import paho.mqtt.client as mqtt # mosquitto.py is deprecated
import time


class Render_Sample_App_Page(Resource):
    def get(self, id):
        headers = {'Content-Type': 'text/html'}

        if 'User' in session:
            username = session['User']['userName']
            profilePicture = session['User']['profilePicture']

            return make_response(
                render_template('apps/sample_app/sample_app.html',
                                username = username,
                                profilePicture = profilePicture
                                ),
                200, headers
            )
        else:
            return make_response(
                redirect('/login')
            )


class Sample_App_Set_Status(Resource):
    def get(self, status):
        print 'status :'+status
        mqttc=mqtt.Client()
        mqttc.connect("127.0.0.1" ,1883, 60)
        #mqttc.subscribe("test/", 2) # <- pointless unless you include a subscribe callback
        mqttc.loop_start()

        device_id = "01"
        subscribe_topic = "led_state_" + device_id

        while True:
            mqttc.publish(subscribe_topic, status)
            time.sleep(1)
            break
