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

def turnstile_pushed():
    return is_button_pressed(turnstile_pushed_button)

def coin_insered():
    return is_button_pressed(coin_inserted_button)

#Initialise systems
state = state_locked
lock_turnstile()

state2 = state2_on
turn_on()

while True:
    if state == state_locked:
        if coin_insered():
            unlock_turnstile()
            state = state_unlocked
    elif state == state_unlocked:
        if turnstile_pushed():
            lock_turnstile()
            state = state_locked

    if state2 == state2_on:
        if button_off_pressed():
            turn_off()
            state2 = state2_off
    elif state2 == state2_off:
        if button_on_pressed():
            turn_on()
            state2 = state2_on
 
