from gpiozero import Servo
from time import sleep

servoPan = Servo(26)
servoTilt = Servo(6)

def Pan():
  servoPan.min()
  sleep(1)
  servoPan.mid()
  sleep(1)
  servoPan.max()
  sleep(1)

def Tilt():
  servoTilt.min()
  sleep(1)
  servoTilt.mid()
  sleep(1)
  servoTilt.max()
  sleep(1)


while True:
  Pan()
  sleep(1)
  Tilt()
  sleep(1)
