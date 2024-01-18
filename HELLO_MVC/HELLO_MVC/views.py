from anaconda_navigator.utils.py3compat import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from HELLO_MVC.dao_emp import DaoEmp


def emp_list(request):
    list = DaoEmp().selectList()
    data = {
        'list' : list
    }
    return render(request, 'emp_list.html', data)

def emp_detail(request):
    e_id = request.GET["e_id"]
    vo = DaoEmp().select(e_id)
    data = {
        'vo' : vo
    }
    return render(request, 'emp_detail.html', data)


def emp_add(request):
    return render(request, 'emp_add.html')

def emp_add_act(request):
    e_id = request.POST["e_id"]
    e_name = request.POST["e_name"]
    gen = request.POST["gen"]
    addr = request.POST["addr"]
    
    cnt = DaoEmp().insert(e_id, e_name, gen, addr)
    data = {
        'cnt' : cnt
    }
    return render(request, 'emp_add_act.html', data)

def emp_mod(request):
    e_id = request.GET["e_id"]
    
    vo = DaoEmp().select(e_id)
    data = {
        'vo' : vo
    }
    return render(request, 'emp_mod.html', data)

def emp_mod_act(request):
    e_id = request.POST["e_id"]
    e_name = request.POST["e_name"]
    gen = request.POST["gen"]
    addr = request.POST["addr"]
    
    cnt = DaoEmp().update(e_id, e_name, gen, addr)
    data = {
        'cnt' : cnt
    }
    return render(request, 'emp_mod_act.html', data)

def emp_del_act(request):
    e_id = request.POST["e_id"]
    
    cnt = DaoEmp().delete(e_id)
    data = {
        'cnt' : cnt
    }
    return render(request, 'emp_del_act.html', data)