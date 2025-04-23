from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_dept(request):
    dno=input('enter deptno:')
    # dto=dEPT.objects.filter(deptno=dno)
    dn=input('enter dname:')
    dl=input('enter dloc:')
    tdo=dept.objects.get_or_create(deptno=dno,dname=dn,loc=dl)
    if tdo[1]:
        QLDO=dept.objects.all()
        d={'QLDO':QLDO}
        return render(request,'display_dept.html',d)
    else:
        return HttpResponse(f'{dn} is already exists')
        
     
def insert_emp(request):
    eno=int(input('enter empno:'))
    en=input('enter ename:')
    job=input('job:')
    sal=int(input('enter salary:'))
    comm=input('enter commission:')
    if comm:
        comm=float(comm)
    else:
        comm=None
    deptno=int(input('deptno:'))
    DO=dept.objects.get(deptno=deptno)
    mgr=input('mgr')
    if mgr:
        MO=emp.objects.get(empno=int(mgr))
    else:
        MO=None
    hiredate=input('date')
    TEO=emp.objects.get_or_create(empno=eno,ename=en,job=job,sal=sal,comm=comm,hiredate=hiredate,deptno=deptno)
    if TEO[1]:
        return HttpResponse(f'{en} is created')
    else:
        return HttpResponse(f'{en} is already exists')
    
    
def display_dept(request):
    QLDO=dept.objects.all()
    d={'QLDO':QLDO}
    return render(request,'display_dept.html',d)

def display_emp(request):
    from django.db.models import Q
    QLEO=emp.objects.filter(deptno=30 , job='CLERK')
    d={'QLEO':QLEO}
    return render(request,'display_emp.html',d)