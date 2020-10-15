from django.db import models
from django.contrib.auth.models import User
from registration.models import Student


class Csv(models.Model):
    term_choices = (
        ('First Term', 'First Term'),
        ('Second Term', 'Second Term'),
        ('Third Term', 'Third Term'),
    )
    subject_choices = (
        ('English', 'English'),
        ('Mathematics', 'Mathematics'),
        ('Agricultural Science', 'Agricultural Science'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Biology', 'Biology'),
        ('Literature-In-English', 'Literature-In-English'),
        ('Commerce', 'Commerce'),
        ('Economics', 'Economics')
    )
    class_choices = (
        ('JSS1', 'JSS1'),
        ('JSS2', 'JSS2'),
        ('JSS3', 'JSS3'),
        ('SSS1', 'SSS1'),
        ('SSS2', 'SSS2'),
        ('SSS3', 'SSS3'),
    )
    subject = models.CharField(max_length=50, choices=subject_choices)
    _class = models.CharField(max_length=50, choices=class_choices)
    session = models.CharField(max_length=20)
    term = models.CharField(max_length=50, choices=term_choices)
    csv = models.FileField(upload_to='media/csvs')
    uploaded_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    activated = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        session_term = f'{self.term} {self.session} {self.subject} for {self._class}'
        return session_term


class Result(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.CharField(max_length=20)
    session = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    first_ca = models.PositiveIntegerField()
    second_ca = models.PositiveIntegerField()
    third_ca = models.PositiveIntegerField()
    exam = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        name = f'{self.term} {self.subject} result for {self.student}'
        return name
