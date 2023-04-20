from django.urls import path, include
from login import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.user_login, name="login"),
    path('signup', views.signup, name="signup"),
    path('doctor', views.doctor_dash, name="doctor_dashboard"),
    path('patient', views.patient_dash, name="patient_dashboard"),
    path('logout', views.logout_user, name="logout"),



]