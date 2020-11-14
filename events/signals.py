from django.core.signals import request_finished
from django.dispatch import receiver
from .models import Notice


@receiver(request_finished, sender=Notice)
def mark_as_read(sender, instance, **kwargs):
    print('works')
