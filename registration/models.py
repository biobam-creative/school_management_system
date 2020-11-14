from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Subject(models.Model):
    subject = models.CharField(max_length=50)
    teachers = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.subject


class Teacher(models.Model):
    title_choices = (
        ('MR', 'MR'),
        ('MRS', 'MRS'),
        ('CHIEF', 'CHIEF'),
        ('PASTOR', 'PASTOR'),
        ('REV', 'REV'),
        ('EVANG', 'EVANG'),
        ('DR', 'DR'),
        ('PROF', 'PROF'),
    )
    gender_choices = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    priviledge = models.BooleanField(default=True)
    title = models.CharField(
        max_length=20, choices=title_choices, default='MALE')
    gender = models.CharField(
        max_length=20, choices=gender_choices, default='MR')
    subjects_taught = models.ForeignKey(Subject, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.DateField()
    religion = models.CharField(max_length=50)
    joining_date = models.DateField()
    class_taught = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    picture = models.ImageField(
        upload_to='registration/images', blank=True, default='registration/images/0011.jpg')
    signature = models.ImageField(
        upload_to='registration/images', blank=True)

    def __str__(self):
        fullname = f'{self.user.first_name} {self.user.last_name}'
        return fullname


class StudentClass(models.Model):
    section_choices = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    )
    title = models.CharField(max_length=10)
    section = models.CharField(max_length=10, choices=section_choices)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    religion = models.CharField(max_length=255)
    section = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=255)
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    admission_date = models.DateField()
    date_of_birth = models.DateField()
    picture = models.ImageField(
        upload_to='registration/images', default='registration/images/0011.jpg')
    parent_contact = models.CharField(max_length=11,)

    def __str__(self):
        fullname = f'{self.user.first_name} {self.user.last_name}'
        return fullname


class Session(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Term(models.Model):
    term_choices = (
        ('First Term', 'First Term'),
        ('Second Term', 'Second Term'),
        ('Third Term', 'Third Term'),
    )
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    term = models.CharField(choices=term_choices, max_length=20)
    school_fee = models.PositiveIntegerField(default=10000)

    def __str__(self):
        return f'{self.session}  {self.term}'
