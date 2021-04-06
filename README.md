# Drone-Simulation

# Dronekit-sitl, MavProxy and QGroundControl 
![90dd4b14-7e22-11e5-9592-5925348a7df9](https://user-images.githubusercontent.com/68418846/113554975-ca74d280-9617-11eb-8d56-2cf0cc227472.png)
## Overview


DroneKit-Python (formerly DroneAPI-Python) contains the python language implementation of DroneKit.

The API allows developers to create Python apps that communicate with vehicles over MAVLink. It provides programmatic access to a connected vehicle's telemetry, state and parameter information, and enables both mission management and direct control over vehicle movement and operations. DroneKit-SITL is the fastest and easiest way to run SITL on Windows, Linux, or MAC OSX. 

The SITL (Software In The Loop) simulator allows you to create and test DroneKit-Python apps without a real vehicle. The ArduPilot SITL simulator allows you to simulate an ArduPilot based autopilot and communicate with it using MAVLink over the local IP network.

## Getting Started
Download or clone the project from github

```sh
$ git clone https://github.com/nityansuman/marvin.git
```
Install prerequisites
```sh
$ pip install -r requirements.txt
```
## Start machine manually
Run project 1 :

```sh
$ cd dronekit
$ python3 sim-manual.py
```

### Screenshots:

- Define the area:

![Screenshot from 2021-04-06 11-45-42](https://user-images.githubusercontent.com/68418846/113668688-3e72b180-96d0-11eb-8720-0b2357f8b082.png)

- Start drone toward 1st waypiont :

![Screenshot from 2021-04-06 11-46-42](https://user-images.githubusercontent.com/68418846/113668724-4894b000-96d0-11eb-8a43-da48078bb459.png)

- Taking pictures :

![Screenshot from 2021-04-06 11-48-45](https://user-images.githubusercontent.com/68418846/113668738-4df1fa80-96d0-11eb-853a-0ec4d3f657a9.png)

- Drone flight plan completed

![Screenshot from 2021-04-06 11-56-14](https://user-images.githubusercontent.com/68418846/113668756-564a3580-96d0-11eb-97c6-6b57dd5577cb.png)

- Download telemetry data :

![Screenshot from 2021-04-06 12-00-27](https://user-images.githubusercontent.com/68418846/113668775-5e09da00-96d0-11eb-92c1-6b1ddd08eba0.png)

## Controlling drone with keyboard arrows
Run project 2 :

```sh
$ cd dronekit
$ python3 sim-conroller.py
```

### Screenshots:

![Screenshot from 2021-04-06 12-27-53](https://user-images.githubusercontent.com/68418846/113671662-4b919f80-96d4-11eb-9bb3-64e278789587.png)
![Screenshot from 2021-04-06 12-28-59](https://user-images.githubusercontent.com/68418846/113671679-4fbdbd00-96d4-11eb-91c0-2072c430db56.png)
- Controlling with arrow keys
![Screenshot from 2021-04-06 12-31-58](https://user-images.githubusercontent.com/68418846/113671693-53e9da80-96d4-11eb-8006-1be315d3764d.png)
- mission completed only if press r to return to the landing point 
![Screenshot from 2021-04-06 12-32-34](https://user-images.githubusercontent.com/68418846/113671710-5ba97f00-96d4-11eb-9be1-6b69e2bc985a.png)


