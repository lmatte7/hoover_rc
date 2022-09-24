import time
from math import atan2, degrees
import board
import adafruit_lsm303dlh_mag
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)
kit = MotorKit(i2c=board.I2C())


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


def get_heading(_sensor):
    magnet_x, magnet_y, _ = _sensor.magnetic
    return vector_2_degrees(magnet_x, magnet_y)


while True:
    print("heading: {:.2f} degrees".format(get_heading(sensor)))
    #kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
    time.sleep(0.5)
