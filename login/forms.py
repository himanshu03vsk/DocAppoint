import sys
sys.path.append("..")
from django import forms
from django.contrib.auth.forms import UserCreationForm
from. models import People, PeoplePhoto

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

