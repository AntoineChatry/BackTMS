import paho.mqtt.client as mqtt
import json, time, random
from datetime import datetime
from time import sleep

#Paramètres de connexion à compléter
#Nom du groupe sans espaces avec la nomenclature WEB2 ou WEB3
#Exemple : WEB2-GROUPE3
GROUPNAME="WEB2-GROUPE5"


MQTT_BROKER="hetic.arcplex.fr"

#Login et mot de passe du groupe
MQTT_USERNAME="GROUPE5"
MQTT_PASSWORD="29989605"
# un ID différent par Node
NODE_ID=["12345678","7654321"]
#ID du sensor
SENSOR_ID=104

client = mqtt.Client("client")
client.username_pw_set(username=MQTT_USERNAME,password=MQTT_PASSWORD)
client.connect(MQTT_BROKER)

#Type de donnée renvoyée : Random 0 ou 1
VAL_STATE=1

def run(condition):
    # while datetime.now().minute not in {0, 15, 40, 45}:
    #     sleep(1)
    def task():
        for node in NODE_ID:
            MQTT_TOPIC = GROUPNAME + "/" + node + "/" + str(SENSOR_ID)
            MQTT_MSG = json.dumps({"source_address": node, "sensor_id": SENSOR_ID, "tx_time_ms_epoch": int(time.time()),
                               "data": {"value": VAL_STATE}})
            client.publish(MQTT_TOPIC, MQTT_MSG)
            print("MQTT Mis à jour - Node %s Timestamp : %s"%(node,int(time.time())))
    task()
    while condition == True:
        sleep(60*10)
        task()

run(True)