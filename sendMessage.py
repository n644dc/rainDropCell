#!/bin/python3

import os
import sys
import time
import json
import base64
from Hologram.HologramCloud import HologramCloud
from vehicleData import Vehicle


erisCloudTestKey = "6cc9647209d1f184552da4ae39f12443410313d262676ac3428f68547792a16e"
rainDropId = "rd0"

hologram = HologramCloud(dict(), network='cellular')

try:
    conn_result = hologram.network.connect()
except Exception as e:
    print("Cannot Connect to Cell Network")
    print(str(e)) 
    sys.exit(0)


if conn_result == False:
    print('Failed to connect to cell network')
print("Connected to Cell Network")


print("Querying Vehicle")
vehicle = Vehicle()
try:
    vd = vehicle.getAllVehicleData()
    vehicleDataJson = json.dumps(vd) 
except Exception as e:
    print("Error Occured Querying Vehicle")
    print(str(e))
    hologram.network.disconnect()
    sys.exit(0)

jsonBytes = str(vehicleDataJson).encode("ascii") 
base64Bytes = base64.b64encode(jsonBytes) 
jsonStringBase64 = base64Bytes.decode("ascii") 

payload = {"rainDropId": rainDropId, "requestType": "VEHICLE_DATA", "requestBody": jsonStringBase64}


print("sending Message...")
message = json.dumps(payload)


response_code = hologram.sendMessage(message, topics=["vehicleData", "rainDrop"])
print(hologram.getResultString(response_code))
print("Sent.")


hologram.network.disconnect()
print("disconnected")
