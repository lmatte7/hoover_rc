import time
import board
from adafruit_motorkit import MotorKit


kit = MotorKit(i2c=board.I2C())

kit.motor1.throttle = -1
kit.motor2.throttle = 1


time.sleep(4)


kit.motor1.throttle = 0
kit.motor2.throttle = 0

time.sleep(4)

kit.motor1.throttle = 1
kit.motor2.throttle = 1

time.sleep(2)

kit.motor1.throttle = -1
kit.motor2.throttle = 1

time.sleep(4)
kit.motor1.throttle = 0
kit.motor2.throttle = 0
