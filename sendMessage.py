#!/bin/python3

import os
import time
import json
from Hologram.HologramCloud import HologramCloud


erisCloudTestKey = "6cc9647209d1f184552da4ae39f12443410313d262676ac3428f68547792a16e"
rainDropId = "rd0"

hologram = HologramCloud(dict(), network='cellular')
conn_result = hologram.network.connect()

if conn_result == False:
    print('Failed to connect to cell network')
print("Connected to Cell Network")

requestType = "REGISTER_NEW_DROP"
requestBody = "New Rain Drop to Register"
payload = {"rainDropId": rainDropId, "requestType": requestType, "requestBody": requestBody}


print("sending Message...")
message = json.dumps(payload)


response_code = hologram.sendMessage(message, topics=["heartbeat", "rainDrop"])
print(hologram.getResultString(response_code))
print("Sent.")


hologram.network.disconnect()
print("disconnected")
