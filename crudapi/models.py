from django.db import models
from django.utils.timezone import now

# Create your models here.

class TeacherDetail(models.Model):
    name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(max_length=64, unique=True, blank=False)
    phone = models.CharField(max_length=32, unique=True, blank=False)
    institute = models.CharField(max_length=128, blank=False)
    experience = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=128, blank=True)
    linkedin = models.CharField(max_length=64, unique=True, blank=True)
    # created_date = models.DateTimeField(default=now)

    def __unicode__(self):
        return self.name        

class Qualification(models.Model):
    teacher = models.ForeignKey(TeacherDetail, on_delete=models.CASCADE, related_name='teacher_qualifications', blank=True)
    ssc = models.DateField(null=True)
    hsc = models.DateField(null=True)
    honours = models.DateField(null=True)
    master = models.DateField(null=True)
    extra = models.CharField(max_length=128, blank=True)
    # created_date = models.DateTimeField(default=now)
    