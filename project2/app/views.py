from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def esha(request):
    return HttpResponse("esha is beautiful")

def abhinav(request):
    return HttpResponse("abhinav is awesome")

def valen(request):
    return render(request,'valen.html')
