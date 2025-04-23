from django.db import models

# Create your models here.
class Meetings(models.Model):
    Meeting_ID= models.IntegerField( primary_key=True)
    Meeting_Date= models.DateField()
    Meeting_Location=models.CharField(max_length=100)
class Attendees(models.Model):
    Meeting_ID=models.ForeignKey(Meetings,on_delete=models.CASCADE)
    Attendees_ID= models.IntegerField( primary_key=True)
    Employee_Name= models.CharField(max_length=100)
    Designation=models.CharField(max_length=100)
    Email=models.EmailField(default="esha@gamil.com")
class Points(models.Model):
    Attendees_ID=models.ForeignKey(Attendees, on_delete=models.CASCADE)
    Points_Discussed=models.CharField(max_length=1000)
    Point_Type=models.CharField(max_length=100,default="support")
