from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
# Create your models here.


person_type = (("patient", "Patient"), ("doctor", "Doctor"))

class People(AbstractUser):
    email                 = models.EmailField(max_length=254)
    address               = models.TextField(default="Mumbai, India")
    designation           = models.CharField(max_length = 20, choices=person_type)

    object  = UserManager()
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.username
    
CATEGORY_CHOICES = (("mental health", "Mental Health"), ("heart disease", "Heart Disease"), ("covid19", "COVID-19"), ("immunization", "Immunization"))
class Blog(models.Model):
    id                  = models.AutoField(primary_key=True)
    publisher           = models.ForeignKey(People, on_delete=models.CASCADE)
    title               = models.CharField(max_length=255)
    category            = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    summary             = models.CharField(max_length=255)
    content             = models.TextField(default="Some Content")
    draft               = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title
class PeoplePhoto(models.Model):
    people_id          = models.ForeignKey(People, on_delete=models.CASCADE, blank=True)
    image              = models.ImageField(upload_to='images/', verbose_name="image", null=True, blank=True)


    def __str__(self) -> str:
        return self.people_id.username
    

class BlogImage(models.Model):
    blog_id             = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image               = models.ImageField(upload_to='blog_images', verbose_name="Blog Image", null=True, blank=True)


class Appointment(models.Model):
    id                  = models.AutoField(primary_key=True)
    doctor_id           = models.ForeignKey(People, on_delete=models.CASCADE, related_name="doctor_id_ref")
    patient             = models.ForeignKey(People, on_delete=models.CASCADE, related_name="patient_id_ref")
    speciality          = models.CharField(verbose_name= "Required Speciality",max_length=30 ,choices=CATEGORY_CHOICES)
    start_time          = models.DateTimeField(verbose_name="Appointment Time" ,null=True, blank=True)
    end_time            = models.DateTimeField(null=True, blank=True)



