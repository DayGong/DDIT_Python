from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pymysql
import json
from anaconda_navigator.utils.py3compat import request

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django")

@csrf_exempt
def ajax(request):
    #menu = request.POST["menu"]
    #print("menu", menu)
    data = json.loads(request.body)
    print(data['menu'])
    
    # print(data)
    
    #context = {
    #    'result' : data,
    #}
    return JsonResponse({'result' : 'success'})

@csrf_exempt
def axios(request):
    data = json.loads(request.body)
    print(data)
    return JsonResponse(data)

@csrf_exempt
def fetch(request):
    data = json.loads(request.body)
    print(data)
    return JsonResponse(data)