#!/bin/python3

import os
import time
import json
from Hologram.HologramCloud import HologramCloud
from vehicleData import Vehicle


erisCloudTestKey = "6cc9647209d1f184552da4ae39f12443410313d262676ac3428f68547792a16e"
rainDropId = "rd0"

hologram = HologramCloud(dict(), network='cellular')

try:
    conn_result = hologram.network.connect()
except Exception as e:
    pass


if conn_result == False:
    print('Failed to connect to cell network')
print("Connected to Cell Network")


vehicle = Vehicle()
vd = vehicle.getAllVehicleData()
vehicleDataJson = json.dumps(vd)


requestType = "VEHICLE_DATA"
requestBody = vehicleDataJson
payload = {"rainDropId": rainDropId, "requestType": requestType, "requestBody": requestBody}


print("sending Message...")
message = json.dumps(payload)


response_code = hologram.sendMessage(message, topics=["vehicleData", "rainDrop"])
print(hologram.getResultString(response_code))
print("Sent.")


hologram.network.disconnect()
print("disconnected")
