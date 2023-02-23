from django.db import models

# Create your models here.
#Depertment and employee model  creation 

class Depertment(models.Model):
    DepertmentId = models.AutoField(primary_key=True)
    DepertmentName = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.DepertmentName

class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Depertment = models.CharField(max_length=500)
    DataOfJoining = models.DateField()
    photoFileName = models.CharField(max_length=400)
    
    def __str__(self) -> str:
        return self.EmployeeName
    

    
