#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import TouchSensor
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

ev3 = EV3Brick()

touch_a = TouchSensor(Port.S1)

motor_a = Motor(Port.A)


while True:
    if touch_a.pressed() == True:
        motor_a.run(1000)
        ev3.screen.clear()
        ev3.screen.print(motor_a.angle())
    else:
        motor_a.run(-1000)
        ev3.screen.clear()
        ev3.screen.print(motor_a.angle())
    wait(100)