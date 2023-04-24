from django.urls import path, include
from login import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.user_login, name="login"),
    path('signup', views.signup, name="signup"),
    path('doctor', views.doctor_dash, name="doctor_dashboard"),
    path('patient', views.patient_dash, name="patient_dashboard"),
    path('logout', views.logout_user, name="logout"),
    path('new_blog', views.new_blog, name="new_blog"),
    path('view_blogs', views.view_blogs, name="view_blogs"),
    path('blog/<int:blog_id>', views.view_ex_blog, name="view_ex_blog"),
    path('save_draft/<int:draft_id>', views.save_draft, name="save_draft"),
    path('doctor/drafts', views.view_drafts, name="view_drafts"),
    path('doctor/edit_draft/<int:blog_id>', views.edit_draft, name="edit_draft"),
    path('categories/<str:category>', views.view_category_blogs, name="view_category_blogs"),



]