from django.urls import path
from . import views

app_name = 'exams_results'

urlpatterns = [
    path('', views.result, name='result')
]
