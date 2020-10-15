from django.shortcuts import render
from .models import Course, Category


def courses(request):
    courses = Course.object.all()
    return render(request, 'online_courses/all_courses.html', {'courses': courses})
