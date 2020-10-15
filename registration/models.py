from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    priviledge = models.BooleanField(default=True)
    subjects_taught = models.CharField(max_length=255)
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

    def __str__(self):
        fullname = f'{self.user.first_name} {self.user.last_name}'
        return fullname


class Student(models.Model):
    student_class_choices = (

        ('JSS1', 'JSS1'),
        ('JSS2', 'JSS2'),
        ('JSS3', 'JSS3'),
        ('SSS1', 'SSS1'),
        ('SSS2', 'SSS2'),
        ('SSS3', 'SSS3'),

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    religion = models.CharField(max_length=255)
    section = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=255)
    student_class = models.CharField(
        max_length=255, choices=student_class_choices)
    admission_date = models.DateField()
    date_of_birth = models.DateField()
    picture = models.ImageField(
        upload_to='registration/images', null=True, default='registration/images/0011.jpg')
    parent_contact = models.CharField(max_length=11,)

    def __str__(self):
        fullname = f'{self.user.first_name} {self.user.last_name}'
        return fullname
