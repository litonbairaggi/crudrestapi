from django.contrib import admin

from . models import TeacherDetail, Qualification
# Register your models here.

@admin.register(TeacherDetail)
class TeacherDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'institute', 'experience', 'address', 'linkedin']

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'ssc', 'hsc', 'honours', 'master', 'extra']
     
    
