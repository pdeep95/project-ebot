from django.shortcuts import render
from django.http import HttpResponse
# from . import hardware

def index(request):
    # return HttpResponse("Index Page")
    return render(request, 'index.html')

def navigate(request):
    if request.GET:
        dir = request.GET['dir']
        if dir in ['left','right','straight','stop']:
            return HttpResponse("valid " + dir)
    return HttpResponse(dir)