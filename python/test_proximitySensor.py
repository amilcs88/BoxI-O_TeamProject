import RPi.GPIO as GPIO
import time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)

while True:
	sensor = GPIO.input(17) #reads from the sensor
	
	if sensor == 1: #this means there is no signal
		print("We ain't seein shit cuz")
		sleep(1)
	elif sensor == 0: #this means there is a signal
		print("I spotted something!")

