from dronekit import connect

def getVehicleData():

    # Connect to the Vehicle (in this case a UDP endpoint)
    vehicle = connect('/dev/ttyS0', wait_ready=True, baud=921600)

    # vehicle is an instance of the Vehicle class
    "px4_autopilot_version": vehicle.version
    "autopilot_ftp":         vehicle.capabilities.ftp
    "globalLoc":             vehicle.location.global_frame
    "globalLoc_relAlt":      vehicle.location.global_relative_frame
    "localLoc":          vehicle.location.local_frame   
    "attitude":          vehicle.attitude
    "velocity":          vehicle.velocity
    "gps":               vehicle.gps_0
    "groundspeed":       vehicle.groundspeed
    "airspeed":          vehicle.airspeed
    "gimbalStatus":      vehicle.gimbal
    "battery":           vehicle.battery
    "ekf_ok":            vehicle.ekf_ok
    "last_heartbeat":    vehicle.last_heartbeat
    "rangefinder":       vehicle.rangefinder
    "rangefinder_distance": vehicle.rangefinder.distance
    "rangefinder_voltage":  vehicle.rangefinder.voltage
    "heading":              vehicle.heading
    "isArmable":            vehicle.is_armable
    "systemStatus":         vehicle.system_status.state
    "mode":                 vehicle.mode.name
    "armed":                vehicle.armed
