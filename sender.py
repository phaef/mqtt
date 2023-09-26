# !/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import configparser
from datetime import datetime

def getConfig():
    configParser = configparser.RawConfigParser()   
    configFilePath = r'config.cfg'
    configParser.read(configFilePath)
    return configParser

if __name__ == "__main__":

    cfg = getConfig()

    TOPIC = cfg.get('MQTT', 'TOPIC')
    BROKER_ADDRESS = cfg.get('MQTT', 'BROKER_ADDRESS')
    PORT = cfg.getint('MQTT', 'PORT')
    QOS = cfg.getint('MQTT', 'QOS')
 
    DATA = f"Current date and time: {datetime.now()}"

    client = mqtt.Client()
    client.connect(BROKER_ADDRESS, PORT)

    print("Connected to MQTT Broker: " + BROKER_ADDRESS)

    client.publish(TOPIC, DATA, qos=QOS)
    client.loop()