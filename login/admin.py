from django.contrib import admin

# Register your models here.


# from django.c/ontrib import admin
from .models import People, PeoplePhoto

# Register your models here.
admin.site.register(People)
admin.site.register(PeoplePhoto)
