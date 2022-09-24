import time
from math import atan2, degrees


import RPi.GPIO as GPIO
import board
GPIO.setmode(GPIO.BCM)

import adafruit_lsm303dlh_mag
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)
kit = MotorKit(i2c=board.I2C())

iTriggerPin = 23
iEchoPin    = 24

GPIO.setup(iTriggerPin, GPIO.OUT)
GPIO.setup(iEchoPin, GPIO.IN)

GPIO.output(iTriggerPin, False)
time.sleep(0.5)

def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


def get_heading(_sensor):
    magnet_x, magnet_y, _ = _sensor.magnetic
    return vector_2_degrees(magnet_x, magnet_y)

def get_distance(triggerPin, echoPin):
  GPIO.output(iTriggerPin, True)
  # Pins connected to the HC-SR04 sensor
  time.sleep(0.0001)
  GPIO.output(triggerPin, False)

  while GPIO.input(echoPin) == 0:
          pass
  fPulseStart = time.time()

  while GPIO.input(echoPin) == 1:
          pass
  fPulseEnd = time.time()

  fPulseDuration = fPulseEnd - fPulseStart

  fDistance = round((fPulseDuration * 17150), 2)

  print("Distance:", fDistance, "cm.")

  time.sleep(0.5)



while True:
    print("heading: {:.2f} degrees".format(get_heading(sensor)))
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
    get_distance(iTriggerPin, iEchoPin)
    time.sleep(0.5)

