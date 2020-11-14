from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('', views.student_payment_info, name='student_payment_info')
]
