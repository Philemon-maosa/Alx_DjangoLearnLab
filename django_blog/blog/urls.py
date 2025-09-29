from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # homepage
    path('', views.home, name='home'),

    # authentication (use Django’s default "registration" folder convention)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),

    # registration (custom view)
    path('register/', views.register, name='register'),

    # profile
    path('profile/', views.profile, name='profile'),
]
