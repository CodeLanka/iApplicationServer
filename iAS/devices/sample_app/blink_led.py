import  paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

#Variables
pin = 12

def on_subscribe(mosq, obj, mid, granted_qos):
    print 'Subscribed to : ' + str(mid) + " " + str(granted_qos)

def on_message(mosq, obj, msg):
    print msg.topic
    print msg.payload
    msg_payload = msg.payload
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    if msg_payload == 'on':
        print "led on"
        GPIO.output(pin,GPIO.HIGH)

    elif msg_payload == 'off':
        print "led off"
        GPIO.output(pin,GPIO.LOW)

device_id = "01"
subscribe_topic = "led_state_" + device_id

client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect("192.168.10.1", 1883, 5)

client.subscribe(subscribe_topic, 0)

client.loop_forever()
