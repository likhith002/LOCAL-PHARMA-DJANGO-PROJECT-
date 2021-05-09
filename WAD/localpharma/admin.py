from django.contrib import admin
from .models import customer,pharmacyowner,medicine,contactus,pharmacymedicine

# Register your models here.

admin.site.register(customer)
admin.site.register(pharmacyowner)
admin.site.register(medicine)
admin.site.register(contactus)
admin.site.register(pharmacymedicine)
