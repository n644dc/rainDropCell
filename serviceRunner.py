#!/usr/bin/python3
import time
from subprocess import Popen, PIPE
import sys, os, glob

class ProcRun:
  def __init__(self):
    pass

  def runCmd(self, cmd):
    proc = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, executable="/bin/bash")
    out, err = proc.communicate()
    return out.decode("utf-8"), err.decode("utf-8")



run = True

procRun = ProcRun()
print("-Running registration send")
output, err = procRun.runCmd("sudo python3 sendMessage.py register")
print("Registration Results")
print("stdout: "+output)
print("ERR: "+err)

# Every 4 minutes - send vehicle data to server via hologram. 
while run:
    print("Sleeping for 4 minutes")
    time.sleep(240)
    try:
        print("-Running Vehicle Data Send")
        output, err = proc.runCmd("sudo python3 sendMessage.py sendVehicleData")
        print("Data Send Results")
        print("stdout: "+output)
        print("ERR: "+err)
    except Exception as e:
        print("Error Occured. Halting.")
        print(str(e))
        sys.exit(0)
    