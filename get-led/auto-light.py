import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 17
GPIO.setup(led, GPIO.OUT)
pin = 6
GPIO.setup(pin, GPIO.IN)
while True:
    state = GPIO.input(pin)
    if state == 0: state = 1
    else: state = 0
    GPIO.output(led, state)
    time.sleep(0.1)