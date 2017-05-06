import sqlite3
conn = sqlite3.connect("alarm.db")
cur = conn.cursor()

def set_alarm(ts):
	query = "insert into reminders (`type`,`about`,`timestamp`) vlaues (?,?,?)"
	cur.execute(query, ('alarm','',ts))
	conn.commit()
	return

def set_reminder(ts,abt):
	query = "insert into reminders (`type`,`about`,`timestamp`) values (?,?,?)"
	cur.execute(query, ('reminder', abt, ts))
	conn.commit()
	return

def set_light(ts, abt):
	query = "insert into reminders (`type`,`about`,`timestamp`) values (?,?,?)"
	cur.execute(query, ('light', abt, ts))
	conn.commit()
	return

