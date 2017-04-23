# this file will be called if user presses button or when user sends request through Mobile phone.
import sys
import subprocess as sp
import requests
import os, time
import speech_recognition as sr
from app.main import *

r = sr.Recognizer()

ERR_MSG = "Sorry Something went wrong"
WAIT_MSG = "Please wait we are processing your request"
pin = 4		# GPIO input PIN
p = None 	# A global process handling variable

def IN():
	OUT("Speak Now ")
	os.system("arecord -D plughw:1 --duration=4 IN.wav")
	print("recorded")
	with sr.AudioFile('IN.wav') as source:
		audio = r.record(source)
	try:
		word = r.recognize_google(audio)
		print("You Said : " + word)
	except sr.UnknownValueError:
		OUT("We didn't get it. Please try again.")
		return None
	except sr.RequestError:
		OUT("Sorry, we need a working internet connection.")
		return None
	return word

def OUT(msg):
	os.system("pico2wave -w OUT.wav \"" + str(msg) + "\"")
	global p
	p = sp.Popen(['aplay','-D','plughw:0','OUT.wav'])
	# os.system("aplay -D plughw:0 OUT.wav")
	time.sleep(2)
	return


if len(sys.argv)>1:
	q = sys.argv[1]
else:
	# user input here (using microphone)
	q = IN()
	if not q:
		sys.exit(0)
	

location = "13.031628,77.6318959"	# should update this with lat,long of HKBKCE

try:
	url = "http://pdeep95.hopto.org:12345/assistant/api/"
	data = {'q': q, 'location': location}
	r = requests.get(url,params=data)
	res = r.json()
	if res['error'] == "None":
		# read result here
		if res['category'] == "hardware":
			if res['type'] == "dict":
				result = res['result']
		# need to add result to db		
		if res['type'] == "single":
			OUT(res['result'])
		elif res['type'] == 'list':
			result=""
			for r in res['result']:
				result = result + str(r) + " \n \n \n \n"
			OUT(result)
		else:
			OUT("Sorry, The result is in tabular form and can not be read.")
	else:
		OUT(res['error'])

except Exception as e:
	OUT(ERR_MSG)


while True:
	if p.poll() != None:
		break
	input_state = io.input(SWITCH)
	if input_state == False:
		p.kill()
		time.sleep(1.5)
		OUT("     Stopped")
		break

