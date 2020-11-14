from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm, LoginForm
from .models import Student, Teacher
from events.models import Event, Notice
from finance.models import SchoolFeeBalance


def home(request):
    return render(request, 'registration/home.html',)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = form.save()
                    Student.objects.create(
                        user=user,
                        student_class=form.cleaned_data['student_class'],
                        picture=form.cleaned_data['picture'],
                        date_of_birth=form.cleaned_data['date_of_birth'],
                        parent_contact=form.cleaned_data['parent_contact'],
                        gender=form.cleaned_data['gender'],
                        father_name=form.cleaned_data['father_name'],
                        religion=form.cleaned_data['religion'],
                        section=form.cleaned_data['section'],
                        father_occupation=form.cleaned_data['father_occupation'],
                        admission_date=form.cleaned_data['admission_date'],

                    )
                    raw_password = form.cleaned_data['password1']
                    user = authenticate(username=user.username,
                                        password=raw_password)
                    login(request, user)
                    return redirect('registration:dashboard')
                except IntegrityError:
                    RegistrationForm()
                    return render(request, 'registration/register.html', {'form': form, 'error': 'Username Has Already Been Taken'})
            else:
                RegistrationForm()
                return render(request, 'registration/register.html', {'form': form, 'error': 'Password do not Match'})
        else:
            RegistrationForm()
            return render(request, 'registration/register.html', {'form': form, 'error': 'Check Your Inputs'})
    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    event = Event.objects.order_by('-date_added')[:5]
    notice = Notice.objects.order_by('-date')[:5]
    students = Student.objects.filter(user=request.user,)
    teachers = Teacher.objects.filter(user=request.user,)
    return render(request, 'registration/dashboard.html', {'students': students, 'teachers': teachers, 'notice': notice, 'event': event})


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('registration:login')


def loginuser(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            form = LoginForm()
            return render(request, 'registration/login.html', {'form': form, 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('registration:dashboard')
