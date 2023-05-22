import time

def customCallback(client,userdata,message):
    print("callback came...")
    print(message.payload)

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


myMQTTClient = AWSIoTMQTTClient("Thing_1")
myMQTTClient.configureEndpoint("ahtwy7llypz0d-ats.iot.ap-south-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("./AmazonRootCA1.pem","./6d0aa8342c83841f71330bb844d6907ae1a7508db4290135a03f9f841e2077e0-private.pem.key", "./6d0aa8342c83841f71330bb844d6907ae1a7508db4290135a03f9f841e2077e0-certificate.pem.crt")


myMQTTClient.connect()
print("Client Connected")

myMQTTClient.subscribe("hari2/tac", 1, customCallback)
print('waiting for the callback. Click to conntinue...')
x = input()

myMQTTClient.unsubscribe("hari2/tac")
print("Client unsubscribed")


myMQTTClient.disconnect()
print("Client Disconnected")
