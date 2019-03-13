from django.contrib import admin
from .models import Student
from django.db import models

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ("School", {'fields': ['school','standard', 'admission_no' ,'roll']}),
        ("Details", {"fields": ['fullname','f_name', 'm_name', 'goal', 'address', 'birth_date', 'blood_group']}),
        ("Contact",{'fields': ['contact', 'social_links', 'profile_pic_link']})
    ]

admin.site.register(Student,StudentAdmin)