from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Naan(request):
    return render(request,'naan.html')

def GarlicBread(request):
    return HttpResponse("Its good with butter chicken")