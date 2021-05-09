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
  `  'default': {  `
       ` 'ENGINE': 'django.db.backends.mysql',`  
  `'NAME': 'localpharma',  `
  `'USER':'root',`  
  `'PASSWORD': 'yourpassword',`  
  `'HOST':'127.0.0.1',`  
  `'PORT':3306`, `
  `}`  
`}`
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
