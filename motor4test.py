import time
import board
from adafruit_motorkit import MotorKit
import RPi.GPIO as GPIO


kit = MotorKit(i2c=board.I2C())



GPIO.setup(17, GPIO.OUT)

GPIO.output(17, GPIO.HIGH)

time.sleep(2)

GPIO.output(17, GPIO.LOW)
