from django.shortcuts import render
from django.Http import HttpResponse
# Create your views here.
def esha(request):
    return HttpResponse("esha.html")

def bharti(request):
    return render(request,"bharti.html")