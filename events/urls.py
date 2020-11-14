from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.notices, name='notices'),
    path('<int:notice_id>', views.notice_detail, name='notice_detail'),
]
