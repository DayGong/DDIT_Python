from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pymysql


# Create your views here.
def index(request):
    return HttpResponse("Hello, World")

def param(request):
    menu = request.GET["menu"]
    return HttpResponse("PARAM:" + menu)

@csrf_exempt
def post(request):
    menu = request.POST["menu"]
    return HttpResponse("POST:" + menu)

def forw(request):
    a = "홍길동"
    b = ["전우치", "이순신", "강감찬"]
    c = [
        {'e_id' : '1', 'e_name' : '1', 'gen' : '1', 'addr' : '1'},
        {'e_id' : '2', 'e_name' : '2', 'gen' : '2', 'addr' : '2'},
        {'e_id' : '3', 'e_name' : '3', 'gen' : '3', 'addr' : '3'},
    ]
    
    data = {
        "a" : a,
        "b" : b,
        "c" : c
    }
    return render(request, 'forw.html', data)

def emp(request):
    conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', 
                       password='python', db='python', charset='utf8')

    cur = conn.cursor(pymysql.cursors.DictCursor) #Dictionary 사전 배열, 연관 배열

    sql = """ 
        SELECT e_id, e_name, gen, addr
        FROM emp
        """
    
    cur.execute(sql)
    result = cur.fetchall()
    
    cur.close()
    conn.close()
    return render(request, 'emp.html', { 'result' : result })