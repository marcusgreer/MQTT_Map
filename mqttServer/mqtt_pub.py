import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time


brokerIP= "169.254.140.49" #"localhost"
brokerPort=1883

client = mqtt.Client(client_id="Laptop Publisher")
client.connect(brokerIP, port=brokerPort)

msg = "34"
for i in range(5):
    client.publish("topics/positions","34")
    print("Message sent")
    time.sleep(10)


