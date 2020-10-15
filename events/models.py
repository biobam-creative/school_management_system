from django.db import models


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
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
