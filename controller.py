import time
import board
from adafruit_motorkit import MotorKit
from pyPS4Controller.controller import Controller

class MyController(Controller):

    kit = MotorKit(i2c=board.I2C())

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
       self.kit.motor1.throttle = 0.5

    def on_x_release(self):
       self.kit.motor1.throttle = 0

    def on_L3_up(self, value):
        print("on_L3_up: {}".format(value))


    def on_L3_down(self, value):
        print("on_L3_down: {}".format(value))

    def on_L3_left(self, value):
        print("on_L3_left: {}".format(value))

    def on_L3_right(self, value):
        print("on_L3_right: {}".format(value))

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
