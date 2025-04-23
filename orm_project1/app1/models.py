from django.db import models

# Create your models here.
class Country(models.Model):
    Country_Code=models.IntegerField(primary_key=True)

class State(models.Model):
    State_Name=models.CharField(max_length=1000,primary_key=True)
    Country_Code=models.ForeignKey(Country, on_delete=models.CASCADE)

class City(models.Model):
    State_Name=models.ForeignKey(State, on_delete=models.CASCADE)
    Pincode=models.IntegerField(primary_key=True)
