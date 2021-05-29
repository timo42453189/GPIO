import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
print('1')
time.sleep(10)
print('End')
GPIO.output(18, GPIO.LOW)
GPIO.cleanup()
