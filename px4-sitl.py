from dronekit import connect, VehicleMode
import plantcv
connection_string = "127.0.0.1:14551"
# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)

# Get some vehicle attributes (state)
print " System status: %s" % vehicle.system_status.state

