import time
import board
from adafruit_motorkit import MotorKit
from pyPS4Controller.controller import Controller

class MyController(Controller):

    kit = MotorKit(i2c=board.I2C())
    max_speed = 0.9
    current_speed = 0

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
       self.kit.motor1.throttle = 0
       self.kit.motor2.throttle = 0
       self.kit.motor3.throttle = 0

    def on_circle_release(self):
         self.kit.motor3.throttle = 0.8

    def on_x_release(self):
       self.kit.motor1.throttle = 0

    def on_L3_up(self, value):
        speed = self.max_speed * ((-1 * value) / 30000)
        self.current_speed = speed
        self.kit.motor1.throttle = speed
        #print("Up: value: {}".format(speed))

    def on_L3_down(self, value):
        speed = -1 * (self.max_speed * (value / 30000))
        self.current_speed =  speed
        self.kit.motor1.throttle = speed

    def on_R3_up(self, value):
        speed = self.max_speed * ((-1 * value) / 30000)
        self.current_speed = speed
        self.kit.motor2.throttle = speed
        #print("Up: value: {}".format(speed))

    def on_R3_down(self, value):
        speed = -1 * (self.max_speed * (value / 30000))
        self.current_speed =  speed
        self.kit.motor2.throttle = speed


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
