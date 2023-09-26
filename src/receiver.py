# !/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import configparser

def getConfig():
    configParser = configparser.RawConfigParser()   
    configFilePath = r'config.cfg'
    configParser.read(configFilePath)
    return configParser

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print("message topic: ", message.topic)
    print("message received: ", msg)

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker: " + BROKER_ADDRESS)
    client.subscribe(TOPIC)

if __name__ == "__main__":

    cfg = getConfig()

    TOPIC = cfg.get('MQTT', 'TOPIC')
    BROKER_ADDRESS = cfg.get('MQTT', 'BROKER_ADDRESS')
    PORT = cfg.getint('MQTT', 'PORT')
    QOS = cfg.getint('MQTT', 'QOS')


    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_ADDRESS, PORT)

    client.loop_forever()