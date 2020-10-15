from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.home, name='home'),
    path('registration', views.register, name='signup'),
    path('login', views.loginuser, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logoutuser, name='logout'),
]
