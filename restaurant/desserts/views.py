from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Brownie_icecream(request):
    return HttpResponse("<h1>Its the best dessert . </h1>")

def Rasmalai(request):
    return render(request,'rasmalia.html')