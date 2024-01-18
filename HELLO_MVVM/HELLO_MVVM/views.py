from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pymysql
import json
from anaconda_navigator.utils.py3compat import request
from HELLO_MVVM.dao_emp import DaoEmp

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django")

@csrf_exempt
def ajax(request):
    data = json.loads(request.body)
    print(data['menu'])
    
    return JsonResponse({'result' : 'success'})

@csrf_exempt
def select_list(request):
    list = DaoEmp().selectList()
    
    return JsonResponse({'list' : list})

@csrf_exempt
def select_one(request):
    data = json.loads(request.body)
    e_id = data['e_id']
    vo = DaoEmp().select(e_id)
    
    return JsonResponse({'vo' : vo})

@csrf_exempt
def insert(request):
    data = json.loads(request.body)
    e_id = data['e_id']
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']
    
    cnt = DaoEmp().insert(e_id, e_name, gen, addr)
    
    return JsonResponse({'cnt' : cnt})

@csrf_exempt
def update(request):
    data = json.loads(request.body)
    e_id = data['e_id']
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']
    
    cnt = DaoEmp().update(e_id, e_name, gen, addr)
    
    return JsonResponse({'cnt' : cnt})

@csrf_exempt
def delete(request):
    data = json.loads(request.body)
    e_id = data['e_id']
    
    cnt = DaoEmp().delete(e_id)
    
    return JsonResponse({'cnt' : cnt})