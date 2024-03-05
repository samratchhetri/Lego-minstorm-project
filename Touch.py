#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import TouchSensor
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

ev3 = EV3Brick()

touch_a = TouchSensor(Port.S1)

while True:
    if touch_a.pressed() == True:
        ev3.screen.clear()
        ev3.screen.print("Pressed")
    else:
        ev3.screen.clear()
        ev3.screen.print("Released")
    wait(100)

