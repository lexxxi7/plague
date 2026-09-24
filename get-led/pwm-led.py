import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 17
GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)
while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)

    duty += 0.1
    if duty > 100.0: duty = 0.0