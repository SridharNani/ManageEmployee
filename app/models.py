from django.db import models

# Create your models here.
class Manager(models.Model):
    email=models.CharField(max_length=30)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    password=models.CharField(max_length=30,)
    address=models.CharField(max_length=30)
    dob=models.DateField()
    company=models.CharField(max_length=30)

class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    email=models.EmailField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    dob = models.DateField()
    company=models.CharField(max_length=30)
    mobile=models.CharField(max_length=12)
    city=models.CharField(max_length=30)
