# Roland2
Web based robot using the V1 Google AIY Voice Hat and a Devastator chassis.
Details of the Voice Hat Google sold as part of the AIY voice kit early 2017.  Replaced by v2 bonnet which doesn't have motor drivers.  You won't be able to duplicate this without additional motor drivers like the ADAfruit motor hat.

# Aim
Use web APIs like AWS Rekognition, Google Vision etc rather than onboard tensorflow like I did with Roland.  Should be simpler and maybe faster.  Trying to use the motor drivers on the hat so that component list is small.  Running on a raspberry Pi.

# Chassis
https://www.robotshop.com/uk/devastator-tank-mobile-robot-platform.html

# Voice hat details
https://pinout.xyz/pinout/voice_hat

# Extras
Standoffs to mount the Pi and speakers.
Small USB hub to make ports accessible.
Short HDMI extension cord to allow access without opening the chassis.
5v Power supply for the Pi, Like a phone charging power pack.
Use a 6V power supply for the motors.
Dupont wires.
Header pins.
Bootlace ferrules for connecting wires.

# Installation
sudo apt install python3-gpiozero

