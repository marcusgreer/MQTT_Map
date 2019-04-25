import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt
import time




def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

#auth = {'username':"afevtheu", 'password':"rdr2nR0R7W4e"}



client = mqtt.Client(client_id="DraNard")
client.on_message=on_message #attach function to callback
client.connect("169.254.140.49", port=1883)
client.subscribe("topics/positions")
client.loop_start()
time.sleep(1000)
client.loop_stop()






