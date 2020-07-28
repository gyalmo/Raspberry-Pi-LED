#WAP to while taking user input (print 1 for green , print 2 for blue , print 3 for yellow)
import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup (18,GPIO.OUT)
GPIO.setup (17,GPIO.OUT)
GPIO.setup (16,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
y=int (input)
If (y==1):
   GPIO.output(18,GPIO.HIGH)
elif (y==2):
   GPIO.output(17,GPIO.HIGH)
else :
   GPIO.output(16,GPIO.HIGH)

