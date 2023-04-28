from django.contrib import admin

# Register your models here.


# from django.c/ontrib import admin
from .models import People, PeoplePhoto,Blog, BlogImage, Appointment

# Register your models here.
admin.site.register(People)
admin.site.register(PeoplePhoto)
admin.site.register(BlogImage)
admin.site.register(Blog)
admin.site.register(Appointment)
