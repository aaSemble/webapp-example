import socket

from django.shortcuts import render
from django.http import HttpResponse

from aasemble_webapp_example.requestlog import models

def index(request):
    models.Request.objects.create(source_ip=request.META['REMOTE_ADDR'], handler=socket.gethostname())
    fmt = '%-33s %-20s %-15s\n'
    out = '20 most recent requests\n'
    out += fmt % ('Time', 'Source IP', 'Handler')
    for req in models.Request.objects.order_by('-timestamp')[:20]:
        out += fmt % (req.timestamp, req.source_ip, req.handler)
    return HttpResponse(out, content_type='text/plain')

def ping(request):
    return HttpResponse('it works', content_type='text/plain')
