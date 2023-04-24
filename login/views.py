from django.shortcuts import render, redirect
from .forms import PeopleForm, ProfileImageForm, BlogForm, BlogImageForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm #add this


# Create your views here.
from .models import *



def listify(blogs):
	'''This returns the record iteself and its associated image with it in a list'''
	blog_set = {}
	for i in blogs:
		blog_set[i.id] = [i, i.blogimage_set.all()[0]]
	return blog_set

login_url = '/login'

@login_required(login_url=login_url)
def home(request):
	if request.user.designation == "doctor":
		return redirect("doctor_dashboard")
	# if category == "":
		# blogs = Blog.objects.filter(draft=False)
	blogs = Blog.objects.filter(draft=False)
	blog_set = listify(blogs=blogs)
	return render(request, "index.html", {'blog_set': blog_set})
	# return redirect("patient_dashboard")

def view_category_blogs(request, category):
	blogs = Blog.objects.filter(draft=False, category=category)
	blog_set = {}
	for i in blogs:
		blog_set[i.id] = [i, i.blogimage_set.all()[0]]
	return render(request, "category_blog.html", {"blog_set": blog_set})

	
	return render(request, 'category_blog.html', {'blog_set', blog_set})


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


@login_required(login_url=login_url)
def save_draft(request, draft_id=None):
	if request.method == "POST":
		photos = request.FILES.getlist("image")
		print(request.POST)
		if request.POST.get('action', '').lower() == "edit draft":
			# if request.POST.get('action', '').lower() == "save edited draft":
				draft = Blog.objects.get(pk=draft_id)
				form1 = BlogForm(request.POST, instance=draft)
				image = BlogImage.objects.get(blog_id=draft_id)
				form2 = BlogImageForm(instance=image)
				# if form1.is_valid() and form2.is_valid():
				fs = form1.save(commit=False)
				fs.draft = True
				fs.save()
				if photos:
					for img in photos:
						BlogImage.objects.create(image=img, blog_id=fs)
					image.delete()
				return redirect("view_drafts")
	blog = Blog.objects.get(pk=draft_id)
	print('here')
	blog.draft = False
	blog.save()
	return redirect("view_blogs")



@login_required(login_url=login_url)
def new_blog(request):
	if request.method == "POST":
		if request.POST.get('action', '').lower() == "draft":
			form1 = BlogForm(request.POST)
			form2 = BlogImageForm(request.POST, request.FILES)
			photos = request.FILES.getlist("image")
			if form1.is_valid() and form2.is_valid():
				fs = form1.save(commit=False)
				fs.publisher = request.user
				fs.draft = True
				fs.save()
				for image in photos:
					BlogImage.objects.create(image=image, blog_id=fs)
				return redirect("view_blogs")
			else:
				print(form1.errors, form2.errors)
				return redirect('view_blogs')
		form1 = BlogForm(request.POST)
		form2 = BlogImageForm(request.POST, request.FILES)
		photos = request.FILES.getlist("image")
		if form1.is_valid() and form2.is_valid():
			fs = form1.save(commit=False)
			fs.publisher = request.user
			fs.draft = False
			fs.save()
			for image in photos:
				BlogImage.objects.create(image=image, blog_id=fs)
			return redirect("view_blogs")
		else:
			print(form1.errors, form2.errors)
			return redirect("view_blogs")
	form1 = BlogForm()
	form2 = BlogImageForm()
	return render(request, 'new_blog.html', {"form1": form1, "form2": form2})

@login_required(login_url=login_url)
def edit_draft(request, blog_id):
	draft = Blog.objects.get(pk=blog_id)
	image = draft.blogimage_set.all()[0]
	if request.method=="POST":	
		form1 = BlogForm(request.POST, instance=draft)
		form2 = BlogImageForm(request.POST, request.FILES, instance=image)
		return render(request, "edit_draft.html", {"form1": form1, "form2": form2})

	form1 = BlogForm(instance=draft)
	form2 = BlogImageForm(instance=image)
	return render(request, "edit_draft.html", {"form1":form1, "form2":form2, "blog_id": blog_id})

@login_required(login_url=login_url)
def view_drafts(request):
	blogs = Blog.objects.filter(publisher=request.user, draft=True)
	blog_set = {}
	for i in blogs:
		print(i.blogimage_set.all())
		# break
		blog_set[i.id] = [i, i.blogimage_set.all()[0]]
	return render(request, "view_drafts.html", {"blog_set": blog_set})




@login_required(login_url=login_url)
def view_blogs(request):
	blogs = Blog.objects.filter(publisher=request.user, draft=False)
	blog_set = {}
	for i in blogs:
		print(i.blogimage_set.all()[0])
		blog_set[i.id] = [i, i.blogimage_set.all()[0]]
	return render(request, "view_blogs.html", {"blog_set": blog_set})

@login_required(login_url=login_url)
def view_ex_blog(request, blog_id):
	blog = Blog.objects.get(pk=blog_id)
	return render(request, "view_ex_blog.html", {"blog":[blog, blog.blogimage_set.all()[0]]})

