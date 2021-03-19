from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from localpharma.models import pharmacyowner
from localpharma.models import customer
from localpharma.models import contactus
from localpharma.models import medicine
from django.contrib.auth.models import User ,auth
# Create your views here.


def homepage(request):

    return render(request,'homepage.html')





def commonloginpage(request):

    return render(request,'commonloginpage.html')


def services(request):
    return render(request,'services.html')

  