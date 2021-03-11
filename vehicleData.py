import json
import time
from dronekit import connect



class Vehicle:
    lastDataSnapshot = None

    def __init__(self):
        pass
    
    def getAllVehicleData(self, rainDropId):
        vehicle = connect('/dev/serial0', wait_ready=True, baud=921600)

        self.lastDataSnapshot = [
            {"dropId":                rainDropId},
            {"px4_autopilot_version": str(vehicle.version)},
            {"autopilot_ftp":         str(vehicle.capabilities.ftp)},
            {"globalLoc":             str(vehicle.location.global_frame)},
            {"globalLoc_relAlt":      str(vehicle.location.global_relative_frame)},
            {"localLoc":              str(vehicle.location.local_frame)},
            {"attitude":              str(vehicle.attitude)},
            {"velocity":              str(vehicle.velocity)},
            {"gps":                   str(vehicle.gps_0)},
            {"groundspeed":           str(vehicle.groundspeed)},
            {"airspeed":              str(vehicle.airspeed)},
            {"gimbalStatus":          str(vehicle.gimbal)},
            {"battery":               str(vehicle.battery)},
            {"ekf_ok":                str(vehicle.ekf_ok)},
            {"last_heartbeat":        str(vehicle.last_heartbeat)},
            {"rangefinder":           str(vehicle.rangefinder)},
            {"rangefinder_distance":  str(vehicle.rangefinder.distance)},
            {"rangefinder_voltage":   str(vehicle.rangefinder.voltage)},
            {"heading":               str(vehicle.heading)},
            {"isArmable":             str(vehicle.is_armable)},
            {"systemStatus":          str(vehicle.system_status.state)},
            {"mode":                  str(vehicle.mode.name)},
            {"armed":                 str(vehicle.armed)},
            {"timestamp":             str(time.time())
        ]
        return self.lastDataSnapshot
        
    def queryVehicleDataToJson(self, rainDropId):
        vd = self.getAllVehicleData(rainDropId)
        return json.dumps(vd)
        