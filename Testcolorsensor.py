#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the color sensor.
color_sensor = ColorSensor(Port.S1)

# Dictionary to translate color codes to human-readable color names.
color_names = {
    0: 'No Color',
    1: 'Black',
    2: 'Blue',
    3: 'Green',
    4: 'Yellow',
    5: 'Red',
    6: 'White',
    7: 'Brown'
}

# Continuously detect and display the color.
while True:
    # Get the color number from the sensor.
    color_number = color_sensor.color()

    # Translate the color number to a readable name.
    color_name = color_names.get(color_number, 'Unknown')

    # Clear the display and show the color name.
    ev3.screen.clear()
    ev3.screen.draw_text(50, 60, color_name)

    # Pause briefly before reading the color again.
    wait(500)
