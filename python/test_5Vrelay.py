
import RPi.GPIO as GPIO
import time import sleep

channel = 21 #Or you could use any pin that you would like, just choose 21 for the memes :)

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def solenoids_unlock(pin):
	GPIO.output(pin, GPIO.HIGH)

def solenoids_lock(pin):
	GPIO.output(pin, GPIO.LOW)

if __name__ == '__main__':
	try:
		solenoids_unlock(channel)
		sleep(1)
		solenoids_lock(channel)
		sleep(1)
		GPIO.cleanup()

	except KeyboardInterrupt:
		GPIO.cleanup()
