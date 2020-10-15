from django.urls import path
from . import views

app_name = 'online_courses'

urlpatterns = [
    path('', views.courses, name='courses')
]
