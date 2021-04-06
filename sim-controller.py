from subprocess import call
import time
import os
import signal
print("Start simulator (SITL)")
print("Starting sketch 'ArduCopter'")
print("Starting SITL input")
call(['gnome-terminal', '-e', "python3 sitl.py"])
print("Waiting for connection with ground station(MAVProxy) ....")

if 1:
    time.sleep(10)

call(['gnome-terminal', '-e', "python3 mavproxy.py"])
print("SITL is safely connected with MAVProxy")
print("Waiting for connection with ground station(QGC) ....")
if 1:
    time.sleep(20)
call(['gnome-terminal', '-e', "python3 qgc.py"])
print("SITL is safely connected with QGC")

print("Drone is ready to fly....")

if 1:
    time.sleep(10)

call(['gnome-terminal', '-e', "python3 controller.py --connect 127.0.0.1:14551"])
if 1:
    time.sleep(5)
os.kill(os.getppid(), signal.SIGHUP)
