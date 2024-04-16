#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize the motors
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Initialize the sensors
line_sensor = ColorSensor(Port.S1)
touch_sensor = TouchSensor(Port.S2)

# Initialize the drive base
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Define color threshold for line following
# Assuming a lighter color surface than the black line
BLACK = 9  # Black value might be very low depending on lighting conditions
LIGHT_SURFACE = 65  # Adjust based on your specific lighter surface color value
threshold = (BLACK + LIGHT_SURFACE) / 2

# Set the drive speed
DRIVE_SPEED = 100

def follow_line(reverse=False):
    """ Function to follow line in either direction. """
    multiplier = -1 if reverse else 1
    while not touch_sensor.pressed():
        reflection = line_sensor.reflection()
        deviation = reflection - threshold
        turn_rate = deviation * 2  # Adjust turn rate gain as needed
        robot.drive(multiplier * DRIVE_SPEED, multiplier * turn_rate)
        ev3.light.on(Color.RED)
        wait(10)
    robot.stop()
    ev3.light.on(Color.GREEN)
    wait(2000)  # Wait for 2 seconds at point B

# Main loop waits for touch sensor press to start
while True:
    if touch_sensor.pressed():
        # Wait until the touch sensor is released to avoid multiple detections
        while touch_sensor.pressed():
            wait(10)
        follow_line()

        # Wait for second touch to return
        while not touch_sensor.pressed():
            wait(10)
        follow_line(reverse=True)