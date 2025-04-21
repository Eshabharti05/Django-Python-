from django.shortcuts import render
from django.http import HttpResponse

def eshabharti(request):
    return HttpResponse("you sooo beautiful, brave and bold")

def valentine(request):
    return render(request,"valentine.html")
