# this file will be called if user presses button or when user sends request through Mobile phone.
import sys
import subprocess as sp
import requests
import os

ERR_MSG = "Sorry Something went wrong"
WAIT_MSG = "Please wait we are processing your request"

def IN():
	return

def OUT(msg):
	return


if len(sys.argv)>1:
	q = sys.argv[1]
else:
	# user input here (using microphone)
	pass

location = "13.031628,77.6318959"	# should update this with lat,long of HKBKCE

try:
	url = "http://pdeep95.hopto.org:12345/assistant/api/"
	data = {'q': q, 'location': location}
	r = requests.get(url,params=data)
	res = r.json()
	if res['error'] == "None":
		# read result here
		pass

except Exception as e:
	OUT(ERR_MSG)

