from gpiozero import PWMOutputDevice
from time import sleep
import time
import os
 
pwm = PWMOutputDevice(4)
pwm2 = PWMOutputDevice(17)
def forward(speed=0.5, dur=-1):
  pwm.value = speed
  pwm.on()
  pwm2.value = speed
  pwm2.on()
  if (dur >= 0):
    time.sleep(dur)
    pwm.off()
    pwm2.off()

def leftturn(speed=0.5, dur=-1):
  pwm.value = speed
  pwm.on()
  if (dur >= 0):
    time.sleep(dur)
    pwm.off()

def rightturn(speed=0.5, dur=-1):
  pwm2.value = speed
  pwm2.on()
  if (dur >= 0):
    time.sleep(dur)
    pwm2.off()

while True:
  sleep(1)
  forward(0.5, 2)
  sleep(1)
  rightturn(0.5, 2)
  sleep(1)
  leftturn(0.5, 2)

