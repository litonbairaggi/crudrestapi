from django.contrib import admin

from . models import TeacherDetail
# Register your models here.

@admin.register(TeacherDetail)
class TeacherDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'institute', 'experience', 'address', 'linkedin']
     
    
