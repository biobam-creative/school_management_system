from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_class_choices = (
        ('JSS1', 'JSS1'),
        ('JSS2', 'JSS2'),
        ('JSS3', 'JSS3'),
        ('SSS1', 'SSS1'),
        ('SSS2', 'SSS2'),
        ('SSS3', 'SSS3'),
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
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_classs = models.CharField(
        max_length=255, choices=course_class_choices)
    subject = models.CharField(max_length=255, choices=subject_choices)
    thumb_nail = models.ImageField(upload_to='online_courses/images')
    url = models.URLField(blank=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    video = models.FileField(upload_to='online_courses/videos', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)
