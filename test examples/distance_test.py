import RPi.GPIO as io
import time

io.setmode(io.BCM)

trig = 23
echo = 24

print("distance sensing")
io.setup(trig, io.OUT)
io.setup(echo, io.IN)

io.output(trig, False)
print("waiting for sensor to settle")
time.sleep(2)

io.output(trig, True)
time.sleep(0.00001)
io.output(trig, False)

while io.input(echo) == 0:
	start = time.time()

while io.input(echo) == 1:
	stop = time.time()

print("Distance : " + str(round(((stop-start) * 17150), 2)) + " cm")

io.cleanup()

