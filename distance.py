import time
from math import atan2, degrees
import board
import adafruit_lsm303dlh_mag
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)
kit = MotorKit(i2c=board.I2C())

GPIO.setmode(GPIO.BCM)

def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


def get_heading(_sensor):
    magnet_x, magnet_y, _ = _sensor.magnetic
    return vector_2_degrees(magnet_x, magnet_y)

def get_distance():
  # Pins connected to the HC-SR04 sensor
  iTriggerPin = 23
  iEchoPin    = 24
  time.sleep(0.0001)
  GPIO.output(iTriggerPin, False)

  while GPIO.input(iEchoPin) == 0:
          pass
  fPulseStart = time.time()

  while GPIO.input(iEchoPin) == 1:
          pass
  fPulseEnd = time.time()

  fPulseDuration = fPulseEnd - fPulseStart

  fDistance = round((fPulseDuration * 17150), 2)

  print("Distance:", fDistance, "cm.")

  time.sleep(0.5)




GPIO.setup(iTriggerPin, GPIO.OUT)
GPIO.setup(iEchoPin, GPIO.IN)

GPIO.output(iTriggerPin, False)
time.sleep(0.5)

while True:
    print("heading: {:.2f} degrees".format(get_heading(sensor)))
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
    get_distance()
    time.sleep(0.5)

GPIO.cleanup()
