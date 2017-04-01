import os
import subprocess
import signal
# import psutil
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Process
# from . import hardware

def index(request):
    # return HttpResponse("Index Page")
    return render(request, 'index.html')

def navigate(request):
    if request.GET:
        dir = request.GET['dir']
        if dir == 'straight':
            p = subprocess.Popen(['python','test.py'])
            P = Process(pid=p.pid, direction=dir)
            P.save()
        elif dir == 'stop':
            P = Process.objects.latest('id')
            pid = P.pid
            # P.delete()
            # os.kill(pid, signal.CTRL_C_EVENT) # windows also try signal.CTRL_BREAK_EVENT
            # os.kill(pid, signal.CTRL_BREAK_EVENT)
            os.kill(pid, signal.SIGKILL)        # unix
    return HttpResponse(dir)