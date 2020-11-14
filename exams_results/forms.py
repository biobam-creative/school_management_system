from django import forms
from django.contrib.auth.models import User
from registration.models import Student
from django.db.models import Q
from .models import Csv
from registration.models import Term, Session, StudentClass, Subject, Teacher, Student


class CsvForm(forms.ModelForm):
    subject_choices = Subject.objects.all()
    class_choices = StudentClass.objects.all()
    session_choices = Session.objects.all()
    term_choices = (
        ('First Term', 'First Term'),
        ('Second Term', 'Second Term'),
        ('Third Term', 'Third Term'),
    )

    subject = forms.ModelChoiceField(label='Select Subject', widget=forms.Select(
        attrs={'placeholder': 'Select Subject', 'class': 'form-control'}), queryset=subject_choices, help_text='', to_field_name='subject', initial='')
    for_class = forms.ModelChoiceField(label='Select Class', widget=forms.Select(
        attrs={'placeholder': 'Select Class', 'class': 'form-control'}), queryset=class_choices, help_text='', to_field_name='title', initial='')
    session = forms.ModelChoiceField(label='Select Session', widget=forms.Select(
        attrs={'placeholder': 'Select Session', 'class': 'form-control'}), queryset=session_choices, help_text='', to_field_name='name', initial='')
    term = forms.ChoiceField(label='Select Term', widget=forms.Select(
        attrs={'placeholder': 'Select Term', 'class': 'form-control'}), choices=term_choices, help_text='', initial='',)
    csv = forms.FileField(label='Upload a CSV File', widget=forms.FileInput(
        attrs={'class': 'form-control'}))

    class Meta():
        model = Csv
        fields = ('subject', 'for_class', 'session',
                  'term', 'csv',)


class TermForm(forms.Form):

    session_choices = Session.objects.all()
    term_choices = (
        ('First Term', 'First Term'),
        ('Second Term', 'Second Term'),
        ('Third Term', 'Third Term')
    )
    class_choices = StudentClass.objects.all()

    student_class = forms.ModelChoiceField(label='', widget=forms.Select(
        attrs={'placeholder': 'Select Session', 'class': 'form-control'}), queryset=class_choices, help_text='', to_field_name='title')
    term = forms.ChoiceField(label='', widget=forms.Select(
        attrs={'placeholder': 'Select Term', 'class': 'form-control'}), choices=term_choices,)
