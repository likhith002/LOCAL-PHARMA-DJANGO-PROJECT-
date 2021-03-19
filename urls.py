
from django.urls import path
from . import views

urlpatterns = [
   
    path("",views.homepage),
    path("customer_login.html",views.customer_login),
    path("pharmacy_login.html",views.pharmacy_login),
    path("commonloginpage.html",views.commonloginpage),
    path("homepage.html",views.homepage),
    path("services.html",views.services),
    path("contact.html",views.contact),
    path("reegister_pharmacy.html",views.reegister_pharmacy),
    path("register_customer.html",views.register_customer)

]
