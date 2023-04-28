import sys
sys.path.append("..")
from django import forms
from django.contrib.auth.forms import UserCreationForm
from. models import People, PeoplePhoto, Blog, BlogImage, Appointment
from datetime import datetime, timedelta

CHOICES = (("patient", "Patient"), ("doctor", "Doctor"))


class PeopleForm(UserCreationForm):
    designation = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = People
        fields = ['first_name', 'last_name','username', 'email','address', 'designation']
        widgets = {'firest_name':forms.TextInput(attrs={'class':'form-input'
                ,'required':''},), 
                 'last_name':forms.TextInput(attrs={'class':'form-input'
                ,'required':''}),
                'email':forms.EmailInput(attrs={'class':'form-input', 'required':''}),
                'address':forms.Textarea(attrs={'class':'form-input', 'required':''}),

                'username':forms.TextInput(attrs={'class':'form-input', 'required':''})}


class ProfileImageForm(forms.ModelForm):

    class Meta:
        model = PeoplePhoto
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class':'form-control', 'required': ''}),
        }



class BlogImageForm(forms.ModelForm):

    class Meta:
        model = BlogImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['draft', 'publisher']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['start_time', 'speciality']
        widgets = {'start_time': forms.TextInput(attrs={'type': 'datetime-local', 'min': f"{str(datetime.today())[:-10]}"})}