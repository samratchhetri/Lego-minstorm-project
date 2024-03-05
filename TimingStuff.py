#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color, Port, Stop
from pybricks.ev3devices import TouchSensor, Motor
from pybricks.tools import StopWatch, wait

# Initialize the EV3.
ev3 = EV3Brick()

motor_a = Motor(Port.A)

sw = StopWatch()

wait(100)

sw.reset()
motor_a.dc(100)
time_dc =  sw.time()
motor_a.stop()
print("Dc time:", time_dc)

sw.reset()
motor_a.run(100)
time_run =  sw.time()
motor_a.stop()
print("Run time:", time_dc)

sw.reset()
motor_a.run_time(1000,1000, then=Stop.COAST, wait=True)
time_run_time =  sw.time()
#motor_a.stop()
print("Run_time time:", time_run_time)


sw.reset()
motor_a.run_until_stalled(1000, then=Stop.COAST, duty_limit=50)
time_stall =  sw.time()
#motor_a.stop()
print("Stall time:", time_stall)
