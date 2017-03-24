import RPi.GPIO as io
import time

io.setmode(io.BOARD)

motor1a = 16
motor1b = 18
motor1e = 22

io.setup(motor1a,io.OUT)
io.setup(motor1b,io.OUT)
io.setup(motor1e,io.OUT)

io.output(motor1a, io.HIGH)
io.output(motor1b, io.LOW)
io.output(motor1e, io.HIGH)

time.sleep(5)

io.output(motor1e, io.LOW)

io.cleanup()
