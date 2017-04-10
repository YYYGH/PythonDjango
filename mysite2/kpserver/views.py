#coding:utf-8
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from .datasave import *
import json
import sys

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == "POST":
        dictr = data_process(request)
        dictjson = json.dumps(dictr)
        return HttpResponse(dictjson)
    else:
        dictr = data_process(request)
        dictjson = json.dumps(dictr)
        return HttpResponse(dictjson)
