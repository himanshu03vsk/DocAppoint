from django.shortcuts import render, redirect
from .forms import PeopleForm, ProfileImageForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm #add this


# Create your views here.
from .models import *

login_url = '/login'

@login_required(login_url=login_url)
def home(request):
	if request.user.designation == "doctor":
		return redirect("doctor_dashboard")
	return redirect("patient_dashboard")


def signup(request):
	if request.method == "POST":
		form = PeopleForm(request.POST)
		image_form = ProfileImageForm(request.POST, request.FILES)
		print(form.is_valid() and image_form.is_valid())
		photos = request.FILES.getlist("image")
		print(photos)
		print(form.errors)
		if form.is_valid() and image_form.is_valid():
			user = form.save()
			print(dir(user))
			# user = form.save()
			print('done')
			for image in photos:
				PeoplePhoto.objects.create(image=image, people_id=user)
			# messages.info(request,f'you are now logged in as {username}')
			login(request, user)
			if str(user.designation).lower() == "doctor":
				return redirect("/doctor")
			else:
				return redirect("/patient")
		else:
			print("Error")
			return render(request,"index.html", {'error': form.errors})
					
			
	form = PeopleForm()
	image_form = ProfileImageForm()
	return render(request, "signup.html", {'form':form, 'image_form': image_form})



@login_required(login_url=login_url)
def doctor_dash(request):
	info = People.objects.get(username=request.user)
	# photo = PeoplePhoto.objects.get(people_id=request.user)
	return render(request, "doctor.html", {'info':info, 'photo': info.peoplephoto_set.all()[0]})



@login_required(login_url=login_url)
def patient_dash(request):
	info = People.objects.get(username=request.user)
	# photo = PeoplePhoto.objects.get(people_id=request.user)
	return render(request, "patient.html", {'info':info, 'photo': info.peoplephoto_set.all()[0]})

def user_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data = request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				if user.designation == "patient":
					print('done')
					return redirect("patient_dashboard")
				else:
					login(request, user)
					return redirect('doctor_dashboard')
	form = AuthenticationForm()
	return render(request, "login.html", {'form':form})






def logout_user(request):
	logout(request)
	return redirect("login")
