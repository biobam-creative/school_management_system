from django import forms
from django.contrib.auth.models import User
from registration.models import Student
from django.db.models import Q
from .models import Csv


class CsvForm(forms.ModelForm):
    class Meta():
        model = Csv
        fields = ('subject', '_class', 'session', 'term', 'csv')
