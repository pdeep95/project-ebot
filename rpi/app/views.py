import os
import subprocess
import signal
import RPi.GPIO as io
# import psutil
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Process
# from . import hardware

MOTOR1A, MOTOR1B, MOTOR1E = 18, 23, None        # GPIO pin assignment for motor 1
MOTOR2A, MOTOR2B, MOTOR2E = 24, 25, None        # GPIO pin assignment for motor 2

def index(request):
    # return HttpResponse("Index Page")
    return render(request, 'index.html')

def navigate(request):
    if request.GET:
        dir = request.GET['dir']
        if dir in ['straight','left','right','reverse']:
            p = subprocess.Popen(['python','test.py',dir])
            P = Process(pid=p.pid, direction=dir)
            P.save()
        elif dir == 'stop':
            io.output(MOTOR1A, False)
            io.output(MOTOR1B, False)
            io.output(MOTOR2A, False)
            io.output(MOTOR2B, False)
            P = Process.objects.latest('id')
            pid = P.pid
            # P.delete()
            # in windows os the server is also being stopped because of CTRL+C event
            # os.kill(pid, signal.CTRL_C_EVENT) # windows also try signal.CTRL_BREAK_EVENT
            # os.kill(pid, signal.CTRL_BREAK_EVENT)
            try:
                os.kill(pid, signal.SIGKILL)        # unix
            except OSError:
                pass
    return HttpResponse(dir)
