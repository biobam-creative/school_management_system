from django import forms
from .models import StudentPaymentInfo


class StudentPaymentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentPaymentInfo
        fields = [
            'full_name', 'email', 'phone_number', 'address'
        ]
