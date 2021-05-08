from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from localpharma.models import pharmacyowner
from localpharma.models import customer
from localpharma.models import contactus
from localpharma.models import pharmacymedicine
from localpharma.models import medicine
from django.contrib.auth.models import User ,auth
from django.http import JsonResponse
# Create your views here.



def check_query(request):
    if request.user.is_authenticated:

        if customer.objects.filter(email=request.user.email):
            c=customer.objects.get(email=request.user.email)

            name = c.firstname
            return render(request, 'customer_query.html', {'Name': name})

        else:
            po = pharmacyowner.objects.get(email=request.user.email)
            name = po.firstname

            return render(request, 'pharmacy_query.html', {'Name': name})



    else:

        return render(request,'homepage.html')




def homepage(request):
    return render(request, 'homepage.html')


def pharmacy_query(request):

    return render(request,'pharmacy_query.html')




def autocomplete(request):
    if 'term' in request.GET:
        obj=medicine.objects.filter(name__istartswith=request.GET.get('term'))
        medicines=list()
        for medi_name in obj:
            medicines.append(medi_name.name)

        return JsonResponse(medicines,safe=False)

    return render(request,'pharmacy_query.html')


def customer_search(request):
    if 'term' in request.GET:
        obj=medicine.objects.filter(name__istartswith=request.GET.get('term'))
        medicines=list()
        for medi_name in obj:
            medicines.append(medi_name.name)

        return JsonResponse(medicines,safe=False)

    return render(request,'customer_query.html')




def customer_query(request):

    if request.method=="POST":

        mide=request.POST['mid']

        obj=medicine.objects.get(name=mide)
        medi_data={}
        medi_data["mname"]=obj.manufacturer_name
        medi_data["type"]=obj.type
        medi_data["price"]=obj.price
        medi_data["name"]=obj.name
        medi_data["scomp"]=obj.short_composition
        medi_data["psize"]=obj.pack_size_label
        medi_data["prescription"]=obj.isprescriptionrequired
        medi_data["image"]=obj. image_url

        ceid=request.session['ceid']

        request.session['medicinename']=mide


        po = customer.objects.get(email=ceid)

        name = po.firstname
        cpin=po.pincode


        obj=medicine.objects.get(name=mide)

        pd=pharmacymedicine.objects.filter(mid=mide,pin=cpin)
        for k in range(-5,5,1):
            pd=pd|pharmacymedicine.objects.filter(mid=mide,pin=str(int(cpin)+k))



        parameters={'medi_data':medi_data,'Name':name,'pdetailes':pd}

        return render(request,'customer_query.html',parameters)

    return render(request,'customer_query.html')




def commonloginpage(request):

    return render(request,'commonloginpage.html')









def show_meds(request):

	email=request.session['peid']
	if pharmacymedicine.objects.filter(eid=email):
		queryset=pharmacymedicine.objects.filter(eid=email)
		context={
			'queryset' : queryset,
		}

		return render(request,'medicine.html',context)

	else:
		return render(request,'medicine.html')

def register_customer(request):


    if request.method == "POST":

        username=request.POST['username']
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

        if customer.objects.filter(email=email ).exists():
            messages.info(request,"Email already exists please provide another Email")
            return redirect('/register_customer.html')

        if User.objects.filter(username=username).exists():
            messages.info(request,"Username already exists please provide another")
            return redirect('/register_customer.html')

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already exists please provide another")
            return redirect('/register_customer.html')

        else:
            obj=customer(firstname=firstname, gender=gender,middlename=middlename,lastname=lastname,email=email,DOB=DOB,phone1=phone1,phone2=phone2,city=city,streetno=streetno,state=state,country=country,pincode=pincode)
            obj.save()
            User.objects.create_user(username=username,password=password,email=email).save()
            print("data has been written to DB Successfully")
            return  redirect('/customer_login.html')
    else:
        return render(request,'register_customer.html')

def profile(request):
    if request.user.is_authenticated:

        if customer.objects.filter(email=request.user.email):
           email = request.session['ceid']

           obj=customer.objects.get(email=email)
           data={}
           data["fname"]=obj.firstname
           data["lname"]=obj.lastname
           data["gender"]=obj.gender
           data["pno"]=obj.phone1
           data["city"]=obj.city
           data["state"]=obj.state
           data["country"]=obj.country
           data["email"]=obj.email
           data["DOB"]=obj.DOB
           data["pincode"]=obj.pincode
           return render(request,'customer_profile.html',{'data':data})

        else:
            peid = request.session['peid']

            obj=pharmacyowner.objects.get(email=peid)
            data={}
            data["fname"]=obj.firstname
            data["lname"]=obj.lastname
            data["gender"]=obj.gender
            data["pno"]=obj.phone1
            data["city"]=obj.city
            data["state"]=obj.state
            data["country"]=obj.country
            data["email"]=obj.email
            data["sname"]=obj.shopname
            data["DOB"]=obj.DOB
            data["pincode"]=obj.pincode
            data["license_file"] = obj.license_file
            data["permission_file"] = obj.permission_file
            return render(request,'pharmacy_profile.html',{'data':data})



    else:

        return render(request,'homepage.html')


def customer_login(request):

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            U = User.objects.get(username=username)

            if customer.objects.filter(email=U.email):
                c= customer.objects.get(email=U.email)
                name = c.firstname
                request.session['ceid'] = U.email

                return render(request,'customer_query.html',{'Name':name})

            else:
                messages.info(request, "INVALID CREDENTIALS")
                return render(request, 'customer_login.html')

        else:
            messages.info(request,"INVALID CREDENTIALS")
            return render(request,'customer_login.html')
    else:
        return render(request,'customer_login.html')

def profile_update(request):
    if request.user.is_authenticated:

        if customer.objects.filter(email=request.user.email):  # checking either email is registered or not
            email = request.session['ceid']  # accessing using session
            if request.method == "POST":

                firstname = request.POST['firstname']  # Post method helps to access data from html page
                middlename = request.POST['middlename']
                lastname = request.POST['lastname']
                phone1 = request.POST['phone1']
                phone2 = request.POST['phone2']
                city = request.POST['city']

                streetno = request.POST['streetno']
                state = request.POST['state']
                country = request.POST['country']
                pincode = request.POST['pincode']

                if customer.objects.filter(email=email):
                    obj = customer.objects.get(email=email)
                    obj.firstname = firstname
                    obj.middlename = middlename
                    obj.lastname = lastname
                    obj.phone1 = phone1
                    obj.phone2 = phone2
                    obj.streetno = streetno
                    obj.state = state
                    obj.city = city
                    obj.country = country
                    obj.pincode = pincode
                    obj.save()  # saves data in database

                    return render(request, 'homepage.html')

                else:
                    messages.info(request,
                                  "The information you are updating is not present in your record please add it",
                                  extra_tags='update_error')  # shows messages
                    return render(request, 'edit_custumer_profile.html', )
        else:
            if request.method == "POST":
                firstname = request.POST['firstname']  # Post method helps to access data from html page
                middlename = request.POST['middlename']  # Post method helps to access data from html page
                lastname = request.POST['lastname']
                phone1 = request.POST['phone1']
                phone2 = request.POST['phone2']
                city = request.POST['city']
                streetno = request.POST['streetno']
                state = request.POST['state']
                license_file = request.FILES['license_file']
                permission_file = request.FILES['permission_file']
                country = request.POST['country']
                pincode = request.POST['pincode']
                shopname = request.POST['shopname']
                license_file = request.FILES['license_file']
                permission_file = request.FILES['permission_file']
                peid = request.session['peid']
                if pharmacyowner.objects.filter(email=peid):
                    obj = pharmacyowner.objects.get(email=peid)
                    obj.firstname = firstname
                    obj.middlename = middlename
                    obj.lastname = lastname
                    obj.phone1 = phone1
                    obj.phone2 = phone2
                    obj.license_file = license_file
                    obj.permission_file = permission_file
                    obj.streetno = streetno
                    obj.state = state
                    obj.city = city
                    obj.country = country
                    obj.pincode = pincode
                    obj.shopname = shopname
                    obj.license_file = license_file
                    obj.permission_file = permission_file

                    obj.save()  # saves data in database

                    return render(request, 'homepage.html')

                else:
                    messages.info(request,
                                  "The information you are updating is not present in your record please add it",
                                  extra_tags='update_error')  # shows messages
                    return render(request, 'edit_profile.html', )
                    
                            
def pharmacy_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            U=User.objects.get(username=username)

            if pharmacyowner.objects.filter(email=U.email):
                po=pharmacyowner.objects.get(email=U.email)
                name=po.firstname
                request.session['peid']=U.email
                return render(request,'pharmacy_query.html',{'Name':name})
            else:
                messages.info(request, "INVALID CREDENTIALS")
                return redirect('/pharmacy_login.html')


        else:
            messages.info(request, "INVALID CREDENTIALS")
            return redirect('/pharmacy_login.html')
    else:

        return render(request,'pharmacy_login.html')

def contact(request):
    if request.method =="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        query=request.POST['query']
        obj=contactus(name=name,phone=phone,email=email,query=query)
        obj.save()
        print("data have been written to DB successfully")
        return redirect('/contact.html')

    else:
        return render(request,'contact.html')

def reegister_pharmacy(request):

    if request.method == "POST":

        username=request.POST['username']
        firstname = request.POST['firstname']
        middlename=request.POST['middlename']
        lastname=request.POST['lastname']
        email=request.POST['email']
        gender=request.POST.get('gender',"Male")

        license_file = request.FILES['license_file']
        permission_file = request.FILES['permission_file']
        
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

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists please provide another")
            return redirect('/reegister_pharmacy.html')

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already exists please provide another")
            return redirect('/reegister_pharmacy.html')



        else:

            obj=pharmacyowner(firstname=firstname, gender=gender,middlename=middlename,lastname=lastname,email=email,DOB=DOB,phone1=phone1,phone2=phone2,city=city,streetno=streetno,state=state,country=country,pincode=pincode,shopname=shopname,license_file=license_file,permission_file=permission_file)
            obj.save()
            User.objects.create_user(username=username, password=password, email=email).save()
            print("data has been written to DB Successfully")
            return redirect('/pharmacy_login.html')
    else:
        return render(request,'reegister_pharmacy.html')









def check_change_password(request):

    if request.user.is_authenticated:
        if customer.objects.filter(email=request.user.email):



            return render(request, 'change_password.html')

        else:
            po = pharmacyowner.objects.get(email=request.user.email)


            return render(request, 'change_password.html')





def change_password(request):
    if request.method=="POST":
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            u=User.objects.get(email=request.user.email)
            u.set_password(password2)
            u.save()
            return render(request,'commonloginpage.html')

        else:

            messages.info(request,"Passwords didnot match")

    else:
        return render(request,'changepassword.html')
		


def logout(request):
    auth.logout(request)
    return redirect('homepage.html')



