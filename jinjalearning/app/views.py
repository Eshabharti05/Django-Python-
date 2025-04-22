from django.shortcuts import render
from django.http import HttpResponse

def jinjaaprint(request):
    d={'a':100}
    d1={'a':200,'b':545,'c':10}
    return render(request, 'jinjaa.html',context=d1)
