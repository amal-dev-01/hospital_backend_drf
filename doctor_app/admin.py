from django.contrib import admin
from doctor_app.models import UserDetails,DoctorProfile
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username') 

admin.site.register(UserDetails, UserAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id',) 

admin.site.register(DoctorProfile, DoctorAdmin)