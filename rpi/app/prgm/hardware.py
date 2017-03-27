# import RPi.GPIO as io
import subprocess
import time

MOTOR1A, MOTOR1B, MOTOR1E = 1, 1, 1     # GPIO pin assignment for motor 1
MOTOR2A, MOTOR2B, MOTOR2E = 1, 1, 1     # GPIO pin assignment for motor 2

def move(dir):
    if dir == "left":
        return
