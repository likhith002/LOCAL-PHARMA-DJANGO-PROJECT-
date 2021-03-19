from django.db import models
from django.conf import  settings
# Create your models here.
class pharmacyowner(models.Model):
    firstname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email= models.CharField(max_length=254)

    lisence=models.FileField()
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender = models.CharField(max_length=6 ,choices=gender_choices)
    
    phone1=models.CharField(max_length=10)
    phone2=models.CharField(max_length=10)
    
    shopname = models.CharField(max_length=50)
    DOB=models.DateField()
    password = models.CharField(max_length=16)
    city = models.CharField(max_length=250)
    streetno=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6)


class customer(models.Model):

    firstname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email= models.CharField(max_length=254)

    
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender = models.CharField(max_length=6 ,choices=gender_choices)
    
    phone1=models.CharField(max_length=10)
    phone2=models.CharField(max_length=10)
    

    DOB=models.DateField()
    password = models.CharField(max_length=16)
    city = models.CharField(max_length=250)
    streetno=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6)
