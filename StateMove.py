#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.parameters import Color

from pybricks.ev3devices import TouchSensor
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# Initialize the EV3.
ev3 = EV3Brick()

touch_closed = TouchSensor(Port.S2)
touch_open = TouchSensor(Port.S1)

motor_turnstile = Motor(Port.A)

# state coding:
state_locked = 0
state_open = 1
state_opening = 2
state_closing = 3

## input coding
coin_insert_button = Button.UP
turnstile_pushed_button = Button.DOWN

## output coding
def close_turnstile():
    motor_turnstile.run(-50)
    ev3.screen.clear()
    ev3.screen.print("Turnstile closing")

def open_turnstile():
    motor_turnstile.run(50)
    ev3.screen.clear()
    ev3.screen.print("Turnstile opening")

def closed_turnstile():
    motor_turnstile.brake()
    ev3.screen.clear()
    ev3.screen.print("Turnstile closed")


def opened_turnstile():
    motor_turnstile.brake()
    ev3.screen.clear()
    ev3.screen.print("Turnstile open")



# Red light   = turnstile closed
# Green light = turnstile open

def is_button_pressed(button):
    pressed_buttons = ev3.buttons.pressed()
    if len(pressed_buttons) == 0:
        return False
    else:
        for pressed_button in pressed_buttons:
            if pressed_button == button:
                return True
        return False

cur_state = state_closing
close_turnstile()

while True:
    next_state = cur_state

    if cur_state == state_locked:
        if is_button_pressed(coin_insert_button):
            open_turnstile()
            next_state = state_opening
        else:
            next_state = state_locked
    elif cur_state == state_open:
        if is_button_pressed(turnstile_pushed_button):
            # maybe sleep a bit
            close_turnstile()
            next_state = state_closing
        else:
            next_state = state_open
    elif cur_state == state_closing:
        if touch_closed.pressed():
            closed_turnstile()
            next_state = state_locked
    elif cur_state == state_opening:
        if touch_open.pressed():
            opened_turnstile()
            next_state = state_open

    cur_state = next_state
 
 
