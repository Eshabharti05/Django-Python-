from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ChickenBiryani(request):
    return HttpResponse("<h1>Try Narmada's, Meghana's and Mani's chicken biryani in Banglore </h1>")

def PrawnsBiryani(request):
    return render(request, 'prawns.html')