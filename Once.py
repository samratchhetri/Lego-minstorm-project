#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import TouchSensor
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

ev3 = EV3Brick()

motor_a = Motor(Port.A)

motor_a.run(200)