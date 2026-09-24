import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 17
button = 13
GPIO.setup(button, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
state = 0
while True:
    if GPIO.input(button):
        if state == 0: state = 1
        else: state = 0
        GPIO.output(led, state)
        time.sleep(0.2)

