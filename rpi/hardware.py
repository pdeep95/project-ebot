import sys
import RPi.GPIO as io
import time
from main import *
import subprocess

def distance():
    io.output(TRIG, False)
    io.output(TRIG, True)
    time.sleep(0.00001)
    io.output(TRIG, False)

    while io.input(ECHO) == 0:
        start = time.time()

    while io.input(ECHO) == 1:
        stop = time.time()
    return round(((stop-start) * 17150), 2)

def stop():
    io.output(MOTOR1A, False)
    io.output(MOTOR1B, False)
    io.output(MOTOR2A, False)
    io.output(MOTOR2B, False)
    subprocess.Popen(['espeak','Obstacle Ahead'])
    return

def move(dir):
    if dir == "left":
        io.output(MOTOR1A, True)
        io.output(MOTOR1B, False)
        io.output(MOTOR2A, False)
        io.output(MOTOR2B, True)
        while True:
            if distance() < 20:
                stop()
            	time.sleep(1)
    elif dir == 'right':
        io.output(MOTOR1A, False)
        io.output(MOTOR1B, True)
        io.output(MOTOR2A, True)
        io.output(MOTOR2B, False)
        while True:
            if distance() < 20:
                stop()
		time.sleep(1)
    elif dir == 'straight':
        io.output(MOTOR1A, True)
        io.output(MOTOR1B, False)
        io.output(MOTOR2A, True)
        io.output(MOTOR2B, False)
        while True:
            if distance() < 20:
                stop()
            	time.sleep(1)
    elif dir == 'reverse':
        io.output(MOTOR1A, False)
        io.output(MOTOR1B, True)
        io.output(MOTOR2A, False)
        io.output(MOTOR2B, True)
        while True:
            if distance() < 20:
                stop()
            	time.sleep(1)
    return

if len(sys.argv) > 1:
    dir = sys.argv[1]
    move(dir)

