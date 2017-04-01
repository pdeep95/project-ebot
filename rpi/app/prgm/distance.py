import RPi.GPIO as io
import time

io.setmode(io.BOARD)

TRIG, ECHO  = 1, 1

io.setup(TRIG, io.OUT)
io.setup(ECHO, io.IN)

io.output(TRIG, False)
# time.sleep(2)     # for sensor to settle

io.output(TRIG, True)
time.sleep(0.00001)
io.output(TRIG, False)

while io.input(ECHO) == 0:
    start = time.time()

while io.input(ECHO) == 1:
    stop = time.time()

print(str(round(((stop-start) * 17150), 2)))
# io.cleanup()