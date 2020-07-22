#WAP to toggle n LEDs
#n=3

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup (18,GPIO.OUT)
GPIO.setup (17,GPIO.OUT)
GPIO.setup (16,GPIO.OUT)

