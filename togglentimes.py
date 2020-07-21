#WAP to toggle LED n times

#n=10
import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup (18,GPIO.HIGH)
for i in range (0,10):        #n=10
   GPIO.output(18,GPIO.HIGH)
   time.sleep(3)
   GPIO.output(18,GPIO.LOW)
   time.sleep(3)
