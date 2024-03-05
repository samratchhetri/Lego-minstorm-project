#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.parameters import Color

from pybricks.ev3devices import TouchSensor
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

from pybricks.tools import StopWatch

## Initialize the EV3.
ev3 = EV3Brick()

# Initialise whatever else you need

## state coding for state machine 1:

# Defined by you

## state coding for state machine 2:
state2_on = 0
state2_off = 1

## input coding state machine 1
coin_insert_button = Button.UP
turnstile_pushed_button = Button.DOWN

## helper functions
# Defined by you

## output coding state machine 1
# Defined by you

## output coding state machine 2
def turn_on_led():
    ev3.light.on(Color.RED)

def turn_off_led():
    ev3.light.off()

## start setup for state machine 1
# Defined by you

## start setup for state machine 1
cur_state2 = state2_on
sw_led = StopWatch()
sw_led.reset()
period = 50
turn_on_led()



while True:
    ## State machine 1
    # Defined by you

    ## State machine 2 
    next_state2 = cur_state2

    if cur_state2 == state2_on:
        if sw_led.time() > period:
            turn_off_led()
            sw_led.reset()
            next_state2 = state2_off
        
    elif cur_state2 == state2_off:
        if sw_led.time() > period:
            turn_on_led()
            sw_led.reset()
            next_state2 = state2_on

    cur_state2 = next_state2
