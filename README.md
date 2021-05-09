# WAD PROJECT  GROUP-17

## TITLE    
 **Designing a website that gives information about medicines available in the local** **pharmacy shops**

 
## NAME
 **LOCAL PHARMA**



##  MOTIVATION
**As medicine can be life saver in many cases but many can’t find it in the required time. There have been cases where people wander for days to find required medicine, Our intention is to reduce their pain and hard work through our web application.**




## PROBLEM STATEMENT

**Our application acts as a platform where local pharmacies come together to provide their services to common buyer.**

<hr />


##  MODULE I

#### INSTALLATION  PROCEDURE

#### Cloning Repository
Firstly You have to clone our application for that click [here](https://github.com/likhith002/git.WAD_TEAM.git)  click on code download ZIP file (for cloning directly)  or  go to your git terminal and enter the command 
`git clone https://github.com/likhith002/git.WAD_TEAM.git`
This will create a folder with all HTML,CSS,JS,PYTHON files required  for  the application 

####  Prerequisites
To run the project you must have python(Version 3.8 and above ) and Django(version 3.1.6 and above )  and any Database(In this we have used MySql)  installed in your computer.


#### Changes to be made after cloning repository

 - Create a database named **localpharma** in your DBMS  
 - Run the Query present in **Sqlqueryfile**  in the database localpharma created (If you are using MySql) or load the CSV file **sqlqueryfile_csv** into your database

- Please enable `DEBUG = True` in  WAD/settings.py 
- After that go to Databases dictionary in WAD/settings.py   in that  add your database type ,password ,username ,host and port number
For example
``` py
DATABASES = {  
    'default': {  
       ` 'ENGINE': 'django.db.backends.mysql',`  
  'NAME': 'localpharma',  
  'USER':'root',
  'PASSWORD': 'yourpassword', 
  'HOST':'127.0.0.1',
  'PORT':3306`, 
  `  
}
```


- Now you have to collect the static files by running the command `python manage.py collectstatic `
This command will collect all the static files like CSS,JS,IMAGES and place it in your assets folder (If you make any changes in css or Js or if you  add images again you have to run the command to collect static files )

- You will have a folder called **Media** which containes the files you upload while registration  and there is a folder called **TEMPLATES** (which containes all HTML pages)

- Now you have to migrate your models to Database by using two commands
```  py
> python manage.py makemigrations`
> `python manage.py migrate`
```

The first command will create a **migrations**  folder in your  project directory with **001_initial.py**  with all the fields in models

The second command will create tables in Database with some default tables

- Now its time to run the app  using the command `python manage.py runserver`
This will run your web application on your localserver  127.0.0.1

- You will be able to see the homepage of  the website  where you will be able to see Register ,Login Services and Contact us buttons 

### HOMEPAGE

homepage gives the basic layout of our application containg logo  images of some medicines 

## MODULE 3

In this module we are implementing ***AUTHENTICATION ,LOGIN,EDIT,LOGOUT and CHANGE PASSWORD***.


### Authentication
```py
def customer_login(request): 

     username = request.POST['username']
     password = request.POST['password']
     user = authenticate(request, username=username, password=password)
     if user is not None:
        auth.login(request, user)
        # Render to a Customer query page.
        ...
     else:
        # Return an 'invalid credentials' error message and render to customer login page.
        ...
   ```

The above pseudo code for customer login view.

To log a user in, from a view, use  `login()` It takes an  `HttpRequest`  object and a  `User` object.  `login()`saves the user’s ID in the session, using Django’s session framework.

When a customer gets logged in he goes to customer query page and then if he clicks on home button then he goes to home page.
Now In this home page the customer can see "Hello Customer" and if he clicks on that he will see a dropdown which has four options i.e Your File, Edit Profile, Change Password and Logout.   
When customer clicks on "Search" he will go to "Customer Query Page".

When a pharmacy owner gets logged in he goes to pharmacy query page and then if he clicks on home button then he goes to home page.
Now In this home page the customer can see "Hello Pharmacy Owner" and if he clicks on that he will see a dropdown which has four options i.e Your File, Edit Profile, Change Password and Logout.   
When he clicks on "Search" he will go to "Customer Query Page".
```py
def logout(request):

     logout(request)
     # Redirect to a Homepage page.`
 ```
->The above is pseudo code of logout view.
->It takes an `HttpRequest` object and has no return value.
->When an user gets logged out he gets redirected to homepage.
->Once he gets logged out he will see now login and register buttons not search and 
    " Hello Customer"/"Hello Pharmacy Owner"


### Edit Page
```
def  profile_update(request):

    if request.user.is_authenticated:
     if customer.objects.filter(email=request.user.email):` 
      email = request.session['ceid'] # accessing using session
      if request.method == "POST":
       we take the information and then update it.
       #If the email given is not present we give an error message and
       render to edit customer profile page.
       #This is for customer.
       
     else:
	    if request.method == "POST":
		 #If the email given is not present we give an error message and
		 render to edit profile page.
	     #This is for pharmacy owner
 ```    
    
The above is pseudo code for profile update view. Our application allows the user to  **Edit** his given information. We use post method here to allow the user to put his new information. Email can't be changed once registered. As we use email as a primary key.

### Change Password
```py
`def change_password(request):`

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
   ```
  User is allowed to ***change his password***. User is asked new password two times for conformation if they are same then new password is saved. Else it returns an error message.





### Common Login Page

Here in one page we have two login options.
->Customer Login
->Pharmacy Login
When he gives valid credentials he goes to Customer/Pharmacy Query pages or 
an error message is shown.
