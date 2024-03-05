#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Color
from pybricks.tools import wait


# Different ways of debugging

ev3 = EV3Brick()

#1
print("Hello!")
while ev3.buttons.pressed() == []:
    wait(10)

#2
ev3.light.on(Color.RED)
wait(1000)
while ev3.buttons.pressed() == []:
    wait(10)

#3
ev3.speaker.beep()
wait(1000)
while ev3.buttons.pressed() == []:
    wait(10)

#4
ev3.screen.clear()
ev3.screen.print("Hello")
wait(1000)
while ev3.buttons.pressed() == []:
    wait(10)
