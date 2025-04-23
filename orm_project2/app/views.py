from django.shortcuts import render
from django.Http import HttpResponse
from app.models import *



def insert_topic(request):
    tn=input("enter topic name: ")
    to=Topic.objects.get_or_create(Topic_Name=tn)
    if to[1]:
        return HttpResponse(f'{tn} is created')
    else:
        return HttpResponse(f'{tn} already exixt')
    

