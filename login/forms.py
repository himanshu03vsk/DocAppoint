import sys
sys.path.append("..")
from django import forms
from django.contrib.auth.forms import UserCreationForm
from. models import People, PeoplePhoto



class PeopleForm(UserCreationForm):
	class Meta:
		model = People
		fields = ['first_name', 'last_name','username', 'email','address', 'designation']
		# widgets = {
            # 'profile_photo': forms.ClearableFileInput()
		# }


class ProfileImageForm(forms.ModelForm):

    class Meta:
        model = PeoplePhoto
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'required': ''}),
        }

