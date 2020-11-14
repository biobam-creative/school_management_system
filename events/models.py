from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save


class Event(models.Model):
    title = models.CharField(max_length=100)
    date_of_event = models.DateField()
    date_added = models.DateField(auto_now=True)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class NotificationCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unread_count = models.IntegerField(default=0)

    def __str__(self):
        return f'Notification count for {self.user}'


""" def incr_notification_counter(sender, instance, created, **kwargs):
    if not(created and not instance.read):
        return
    NotificatonControlller(instance.user).update_unread_count(1)


post_save.connect(incr_notification_counter, sender=Notice) """
