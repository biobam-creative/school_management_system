from django.contrib import admin
from .models import Event, Notice, NotificationCount

admin.site.register(Event)
admin.site.register(Notice)
admin.site.register(NotificationCount)
