import datetime
import os
import sqlite3
import subprocess as sp
import time
from app.main import *


conn = sqlite3.connect("alarm.db")
cur = conn.cursor()

cur.execute("select * from reminders where status=0")
rows = cur.fetchall()

tm = datetime.datetime.now().timestamp()
tm = round(tm/60) * 60

def alarm_on():
	for i in range(0,20):
		p = sp.Popen(["aplay","-D","plughw:0","Rooster.wav"])
		while p.poll() != None:
			pass

def reminder_on(text):
	os.system("pico2wave -w REMINDER.wav \"" + str(text) + "\"")
	os.system("aplay -D plughw:0 REMINDER.wav")
	time.sleep(1)
	return


if rows:
	for row in rows:
		if tm < int(row[3]) <= (tm+60):
			if row[1] == "alarm":
				alarm_on()
			elif row[1] == "reminder":
				reminder_on(row[2])

