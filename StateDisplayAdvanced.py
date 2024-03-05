#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.parameters import Color
# Initialize the EV3.
ev3 = EV3Brick()

## state coding:
state_locked = 1
state_unlocked = 2

## input coding
coin_inserted_button = Button.UP
turnstile_pushed_button = Button.DOWN

## output coding
# Red light   = turnstile locked
def lock_turnstile():
    ev3.light.on(Color.RED)

# Green light = turnstile unlocked
def unlock_turnstile():
    ev3.light.on(Color.GREEN)

def is_button_pressed(button):
    pressed_buttons = ev3.buttons.pressed()
    if len(pressed_buttons) == 0:
        return False
    else:
        for pressed_button in pressed_buttons:
            if pressed_button == button:
                return True
        return False

#Initialise system
cur_state = state_locked
lock_turnstile()

while True:
    next_state = cur_state

    if cur_state == state_locked:
        if is_button_pressed(coin_inserted_button):
            unlock_turnstile()
            next_state = state_unlocked

    elif cur_state == state_unlocked:
        if is_button_pressed(turnstile_pushed_button):
            lock_turnstile()
            next_state = state_locked

    else:
        # If we ever reach here, we did something wrong.
        # Every state should be handled explicitly
        abort()

    cur_state = next_state
 
 
