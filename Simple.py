#!/usr/bin/env pybricks-micropython

#Simple program

from pybricks.hubs import EV3Brick
from pybricks.parameters import Color
from pybricks.tools import wait

ev3 = EV3Brick()

while True:
    ev3.light.on(Color.RED)
    wait(1000)
    ev3.light.on(Color.YELLOW)
    wait(1000)