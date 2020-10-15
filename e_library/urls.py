from django.urls import path
from . import views

app_name = 'e_library'

urlpatterns = [
    path('', views.elibrary, name='elibrary')
]
