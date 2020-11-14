from django.db.models.signals import post_save, post_delete
from finance.models import SchoolFeeBalance
from django.dispatch import receiver
from .models import Student, Term


@receiver(post_save, sender=Student)
def create_school_fee_balance(sender, instance, created, **kwargs):
    if created:
        SchoolFeeBalance.objects.create(
            student=instance, balance=0)


@receiver(post_save, sender=Term)
def add_term_fee(sender, instance, created, **kwargs):
    school_fees_balances = SchoolFeeBalance.objects.all()
    if created:
        for school_fees_balance in school_fees_balances:
            print(school_fees_balance.balance)
            school_fees_balance.balance += instance.school_fee
            school_fees_balance.save()
            print(school_fees_balance.balance)
