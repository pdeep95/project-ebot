# this is main file and has to be run first (This actually initializes the RPi GPIOs)
import RPi.GPIO as io
import time


SWITCH = 4      # a switch is connected to pin 4
# let MOTOR1E & MOTOR2E both be high (Vcc)
MOTOR1A, MOTOR1B, MOTOR1E = 18, 23, None        # GPIO pin assignment for motor 1
MOTOR2A, MOTOR2B, MOTOR2E = 24, 25, None        # GPIO pin assignment for motor 2
RED_LED, GREEN_LED = 5,6                        # GPIO pin assignment for red & green leds.
TRIG, ECHO  = 20, 21                            # for distance sensor
MSDA, MSDL = 2, 3                               # for magnetometer

io.setmode(io.BCM)

io.setwarnings(False)

io.setup(MOTOR1A, io.OUT)               # for Motor
io.setup(MOTOR1B, io.OUT)
io.setup(MOTOR2A, io.OUT)
io.setup(MOTOR2B, io.OUT)

io.setup(RED_LED, io.OUT)               # for leds (status)
io.setup(GREEN_LED, io.OUT)

io.setup(TRIG, io.OUT)                  # for Distance Sensor
io.setup(ECHO, io.IN)                   # for Distance Sensor

'''
io.setup(SWITCH, io.IN, pull_up_down=io.PUD_UP)

while True:
    input_state = io.input(SWITCH)
    if input_state == False:
        # do something when the switch is pressed
        # time.sleep(0.2)
        pass
'''
