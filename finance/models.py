from django.db import models
from registration.models import Student, Term


class StudentPaymentInfo(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=150)


class SchoolFeeBalance(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField()

    def __str__(self):
        string = f'{self.student} school fee balance'
        return string
