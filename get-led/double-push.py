import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2
while True:
    change = False
    up_pr = GPIO.input(up)
    down_pr = GPIO.input(down)
    if up_pr and down_pr:
        num = 255
        print(num, dec2bin(num))
        time.sleep(0.3)
        change = True
    elif up_pr:
        num += 1
        if num > 255: num = 0
        print(num, dec2bin(num))
        time.sleep(sleep_time)
        change = True
    elif down_pr:
        num -= 1
        if num < 0: num = 255
        print(num, dec2bin(num))
        time.sleep(sleep_time)
        change = True
    time.sleep(0.05)
    GPIO.output(leds, dec2bin(num))