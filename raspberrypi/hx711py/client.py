import json
import time
import sys
import paho.mqtt.client as paho
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 
client = paho.Client(client_id="pi_device_10")
client.on_publish = on_publish
client.on_connenct = on_connect
client.connect("192.168.43.157", 1883)
client.loop_start()
count = 0;

class Payload:
    deviceID = ""
    appID = ""
    weight = 0
    def __init__(self, deviceID, appID):
        self.deviceID = deviceID
        self.appID = appID
    def setWeight(self,weight):
        self.weight = weight

packet = Payload("A","B")
packet.setWeight(10)

while True:
    client.publish("obol/tare", json.dumps(packet.__dict__), qos=0)
    count = count + 1
    time.sleep(1)

#
## The callback for when a PUBLISH message is received from the server.
#def on_message(client, userdata, msg):
#	print(msg.topic+" "+str(msg.payload))
#
#random_client_id = "1234" 
#client = mqtt.Client(client_id=random_client_id, protocol=mqtt.MQTTv31)
#client.on_connect = on_connect
#client.on_message = on_message
#hive_test = "broker.mqttdashboard.com"
#
#client.connect(hive_test, 1883, 60)
#client.loop_start()
##client.loop_forever()
#payload = { 'properties': [{ 'id': '518be5a700045e1521000001', 'value': "fuck" }] }
#client.publish("yoyo123", json.dumps(payload))

