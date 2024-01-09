# !/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import configparser
import time
from datetime import datetime

CONFIG_FILE="config/configuration.txt"

def getConfig():
    config = {}

    configParser = configparser.ConfigParser()
    configParser.optionxform = str
    configFilePath = CONFIG_FILE
    configParser.read(configFilePath)

    # Iterate over the sections and options
    for section in configParser.sections():
        for option in configParser.options(section):
            # Get the value of the option
            value = configParser.get(section, option)

            # Add the option and value to the config dictionary
            config[option] = value
    return config

if __name__ == "__main__":

    cfg = getConfig()

    # Map dictionary to single values
    TOPIC = str(cfg['TOPIC'])
    BROKER_ADDRESS = cfg['BROKER_ADDRESS']
    PORT = int(cfg['PORT'])
    QOS = int(cfg['QOS'])   
    USER = cfg['USER']
    PASSWORD = cfg['PASSWORD']
 
    data = ""

    client = mqtt.Client()
    client.username_pw_set(USER, PASSWORD)
    client.connect(BROKER_ADDRESS, PORT)

    print("Connected to MQTT Broker: " + BROKER_ADDRESS + ":" + str(PORT))

    while True:
        data = f"Current date and time: {datetime.now()}"

        client.publish(topic=TOPIC, payload=data, qos=QOS)
        client.loop()

        time.sleep(1)