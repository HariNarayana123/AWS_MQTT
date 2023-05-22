from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys

myMQTTClient = AWSIoTMQTTClient("Thing_1")

myMQTTClient.configureEndpoint("ahtwy7llypz0d-ats.iot.ap-south-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("./AmazonRootCA1.pem","./6d0aa8342c83841f71330bb844d6907ae1a7508db4290135a03f9f841e2077e0-private.pem.key", "./6d0aa8342c83841f71330bb844d6907ae1a7508db4290135a03f9f841e2077e0-certificate.pem.crt")

myMQTTClient.connect()
print("Client Connected")

msg = "Hello hari";
topic = "hari/tac"
myMQTTClient.publish(topic, msg, 0)
print("Message Sent")

myMQTTClient.disconnect()
print("Client Disconnected")
