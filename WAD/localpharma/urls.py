
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
    path("register_customer.html",views.register_customer),
    path("pharmacy_query.html",views.pharmacy_query),
    path("add",views.add,name='add'),
    path("edit",views.edit,name='edit'),
    path("delete",views.delete,name='delete'),
    path('autocomplete',views.autocomplete,name='autocomplete'),
    path("customer_query.html",views.customer_query),
    path('customer_search',views.customer_search,name='customer_search'),
    path('logout',views.logout,name='logout'),
    path('check_query',views.check_query,name='check_query'),
    path('check_change_password',views.check_change_password,name='check_change_password'),
    path('change_password.html',views.change_password),
    path('profile',views.profile,name='profile'),
    path('show_meds',views.show_meds,name='show_meds'),
    path('complete_detailes',views.complete_detailes,name='complete_detailes'),
    path("edit_profile.html",views.edit_profile),
    path("update_profile.html",views.profile_update),
    path("edit_customer_profile.html",views.edit_customer_profile),
    path("check_update.html",views.check_update)


]
