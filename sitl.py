import os
import signal
os.system("dronekit-sitl copter ")
if 1:
    time.sleep(2)

os.kill(os.getppid(), signal.SIGHUP)
