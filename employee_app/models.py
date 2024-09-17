from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
class employee(models.Model):
    employeeid=models.IntegerField(primary_key=True,unique=True)
    firstname=models.CharField(max_length=50,unique=True)
    lastname=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50)
    contactnumber=models.CharField(max_length=10)
    department=models.TextField(max_length=100)
    designation=models.TextField(max_length=200)

    def  __str__(self):
        return self.firstname