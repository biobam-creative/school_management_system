from django.contrib import admin
from .models import Teacher, Student, Session, Term, StudentClass, Subject


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Session)
admin.site.register(Term)
admin.site.register(StudentClass)
admin.site.register(Subject)


# Register your models here.
