from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def esha(request):
    return HttpResponse("esha bharti")

def job(request):
    return render(request,'job.html')