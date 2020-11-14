from django.db import models
from django.contrib.auth.models import User
from registration.models import Student, StudentClass, Subject, Term, Session, Teacher
from django.template.defaultfilters import slugify


class Csv(models.Model):
    """ term_choices = (
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
    ) """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    for_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    term = models.CharField(max_length=50)
    csv = models.FileField(upload_to='media/csvs')
    uploaded_by = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, blank=True, null=True)
    activated = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        session_term = f'{self.term} {self.session} {self.subject} for {self.for_class}'
        return session_term


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.CharField(max_length=20)
    session = models.CharField(max_length=50)
    student_class = models.CharField(max_length=50, default='JSS1')
    subject = models.CharField(max_length=50)
    first_ca = models.PositiveIntegerField()
    second_ca = models.PositiveIntegerField()
    third_ca = models.PositiveIntegerField()
    exam = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    remark = models.CharField(max_length=100, blank=True)
    grade = models.CharField(max_length=100, blank=True)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True, max_length=200, null=True)

    def __str__(self):
        name = f'{self.student_class} {self.term} {self.subject} result for {self.student}'
        return name

    def save(self, *args, **kwargs):
        name = f'{self.student_class} {self.term} {self.subject} result for {self.student}'
        self.slug = slugify(name)
        super(Result, self).save(*args, **kwargs)
