#WAP to toggle 3 LEDs using string and taking user input

import Rpi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup (18,GPIO.OUT)
GPIO.setup (17,GPIO.OUT)
GPIO.setup (16,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
print (“ write GREEN,BLUE,YELLOW”)
y= str (input())
If (y== “green” or “GREEN”):
   GPIO.output(18,GPIO.HIGH)
elif (y== “blue” or “BLUE”):
   GPIO.output(17,GPIO.HIGH)
elif (y== “yellow” or “YELLOW”):
   GPIO.output(16,GPIO.HIGH)
else:
   GPIO.output(18,GPIO.LOW)
   GPIO.output(17,GPIO.LOW)
   GPIO.output(16,GPIO.LOW)

