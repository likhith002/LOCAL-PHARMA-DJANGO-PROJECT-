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

def customer_login(request):

    if request.method=="POST":
        email = request.POST['email']
        password=request.POST['password']
        if customer.objects.filter(email=email,password=password):

            return redirect('/homepage.html')

        else:
            messages.info(request,"INVALID CREDENTIALS")
            return redirect('/customer_login.html')
    else:
        return render(request,'customer_login.html')

def pharmacy_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if pharmacyowner.objects.filter(email=email, password=password):

            return redirect('/homepage.html')

        else:
            messages.info(request, "INVALID CREDENTIALS")
            return redirect('/pharmacy_login.html')
    else:

        return render(request,'pharmacy_login.html')


def reegister_pharmacy(request):

    if request.method == "POST":

        firstname = request.POST['firstname']
        middlename=request.POST['middlename']
        lastname=request.POST['lastname']
        email=request.POST['email']
        gender=request.POST.get('gender',"Male")
        
        DOB=request.POST['DOB']
        phone1=request.POST['phone1']
        phone2=request.POST['phone2']
        password=request.POST['password']
        city=request.POST['city']
        streetno=request.POST['streetno']
        state=request.POST['state']
        country=request.POST['country']
        pincode=request.POST['pincode']
        shopname=request.POST['shopname']

        if pharmacyowner.objects.filter(email=email).exists():
            messages.info(request,"Email alredy exists please provide another Email")
            print("Email alredy exists please provide another Email")
            return redirect('/reegister_pharmacy.html')


        else:

            obj=pharmacyowner(firstname=firstname, gender=gender,middlename=middlename,lastname=lastname,email=email,DOB=DOB,phone1=phone1,phone2=phone2,password=password,city=city,streetno=streetno,state=state,country=country,pincode=pincode,shopname=shopname)
            obj.save()
            print("data has been written to DB Successfully")
            return redirect('/pharmacy_login.html')
    else:
        return render(request,'reegister_pharmacy.html')


def register_customer(request):


    if request.method == "POST":


        firstname = request.POST['firstname']
        middlename=request.POST['middlename']
        lastname=request.POST['lastname']
        email=request.POST['email']
        gender=request.POST.get('gender',"Male")
        
        DOB=request.POST['DOB']
        phone1=request.POST['phone1']
        phone2=request.POST['phone2']
        password=request.POST['password']
        city=request.POST['city']
        streetno=request.POST['streetno']
        state=request.POST['state']
        country=request.POST['country']
        pincode=request.POST['pincode']

        if customer.objects.filter(email=email).exists():
            messages.info(request,"Email already exists please provide another Email")
            return redirect('/register_customer.html')

        else:
            obj=customer(firstname=firstname, gender=gender,middlename=middlename,lastname=lastname,email=email,DOB=DOB,phone1=phone1,phone2=phone2,password=password,city=city,streetno=streetno,state=state,country=country,pincode=pincode)
            obj.save()
            print("data has been written to DB Successfully")
            return  redirect('/customer_login.html')
    else:
        return render(request,'register_customer.html')


  