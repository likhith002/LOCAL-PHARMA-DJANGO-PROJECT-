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


class medicine(models.Model):
    manufacturer_name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    short_composition = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    pack_size_label = models.CharField(max_length=100, blank=True, null=True)
    isprescriptionrequired = models.CharField(db_column='isPrescriptionRequired', max_length=30, blank=True, null=True)  # Field name made lowercase.
    url_to_scrape = models.CharField(max_length=255, blank=True, null=True)


class contactus(models.Model):
    name = models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=255)
    query=models.CharField(max_length=255)