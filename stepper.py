import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit(i2c=board.I2C())

while True:
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
    time.sleep(0.3)
