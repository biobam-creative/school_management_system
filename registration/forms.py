from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . models import Student, StudentClass


gender_choices = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

section_choices = (
    ('A', 'A'),
    ('B', 'B'),
)
student_class_choices = StudentClass.objects.all()


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'username', 'placeholder': 'Username', 'class': 'form-control', }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'name': 'password1', 'placeholder': 'Password', 'class': 'form-control', }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'name': 'password2', 'placeholder': 'Confirm Password', 'class': 'form-control', }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'name': 'email', 'placeholder': 'E-mail', 'class': 'form-control', }))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'first_name', 'placeholder': 'First Name', 'class': 'form-control', }))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'last_name', 'placeholder': 'Surname', 'class': 'form-control', }))
    student_class = forms.ModelChoiceField(queryset=student_class_choices,
                                           initial='Class', label='Class', widget=forms.Select(attrs={'name': 'first_name', 'placeholder': 'First Name', 'class': 'form-control', }))
    date_of_birth = forms.DateField(help_text='Format: YYYY-MM-DD', widget=forms.DateInput(
        attrs={'name': 'dob', 'placeholder': 'Date Of Birth', 'class': 'form-control', }))
    picture = forms.ImageField(required=False,
                               help_text='Upload Photo(150px X 150px)')
    parent_contact = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'parent_contact', 'placeholder': 'Guardian Phone Number', 'class': 'form-control', }))
    section = forms.ChoiceField(initial='Section', choices=section_choices,  widget=forms.Select(
        attrs={'name': 'Section', 'placeholder': 'Section', 'class': 'form-control', }))
    admission_date = forms.DateField(help_text='Format: YYYY-MM-DD', widget=forms.DateInput(
        attrs={'name': 'admission_date', 'placeholder': 'Admission Date', 'class': 'form-control', }))
    father_name = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'father_name', 'placeholder': 'Father\'s Name', 'class': 'form-control', }))
    religion = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'religion', 'placeholder': 'Religion', 'class': 'form-control', }))
    father_occupation = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'father_occupation', 'placeholder': 'Father\'s Occupation', 'class': 'form-control', }))
    gender = forms.ChoiceField(initial='Gender', choices=gender_choices,  widget=forms.Select(
        attrs={'name': 'gender', 'placeholder': 'Gender', 'class': 'form-control', }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2',
                  'student_class', 'date_of_birth',
                  'picture', 'parent_contact', 'gender',
                  'father_name', 'religion', 'section',
                  'father_occupation', 'admission_date')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'name': 'username', 'placeholder': 'Email', 'class': 'form-control form-control-sm', }))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'name': 'password', 'placeholder': 'Password', 'class': 'form-control form-control-sm', }))

    class Meta:
        model = User
        fields = ['username', 'password', ]


""" class ProfileForm(forms.ModelForm):
    surname = forms.CharField(label='', widget=forms.TextInput(
        attrs={'name': 'surname', 'placeholder': 'Surname', 'class': 'form-control', }))
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'name': 'student_class', 'placeholder': 'Class', 'class': 'form-control', 'selected': 'Class'}))
    student_class = forms.ModelChoiceField(
        queryset=class_choices, label='', widget=forms.Select(attrs={'name': 'first_name', 'placeholder': 'First Name', 'class': 'form-control', }))
    date_of_birth = forms.DateField(label='', widget=forms.DateInput(
        attrs={'name': 'dob', 'placeholder': 'Date Of Birth', 'class': 'form-control', }))

    class Meta:
        model = Profile
        fields = ("surname", "first_name", "student_class",
                  "date_of_birth", "picture", "parent_contact") """
