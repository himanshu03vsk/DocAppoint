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
    

    
class PeoplePhoto(models.Model):
    people_id          = models.ForeignKey(People, on_delete=models.CASCADE, blank=True)
    image              = models.ImageField(upload_to='images/', verbose_name="image", null=True, blank=True)


    def __str__(self) -> str:
        return self.people_id.username
    

