import RPi.GPIO as GPIO     #this opens the library

GPIO.setmode(GPIO.BCM)      #pins names
GPIO.setwarnings (False)    #instructs Python not to print warning

GPIO.setup(18, GPIO.OUT)    #Raspberry Pi pins 18, 23, and 24
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

print(“Lights on”)          #Python command for lights to turn on
GPIO.output(18, GPIO.HIGH)  #Rpi pins will be given 3.3 volts
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

print(“Lights off”)         #Python command for lights to turn off
GPIO.output(18, GPIO.LOW)   #Rpi pins (-) 3.3 volts
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)

GPIO.cleanup()              #Reset the status of each pins
