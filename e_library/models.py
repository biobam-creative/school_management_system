from django.db import models


class Book(models.Model):
    book_class_choices = (

        ('JSS1', 'JSS1'),
        ('JSS2', 'JSS2'),
        ('JSS3', 'JSS3'),
        ('SSS1', 'SSS1'),
        ('SSS2', 'SSS2'),
        ('SSS3', 'SSS3'),

    )
    title = models.CharField(max_length=255)
    book_class = models.CharField(max_length=255, choices=book_class_choices)
    subjects = models.CharField(max_length=255, default='Mathematics')
    author = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    image = models.ImageField(upload_to='e_library/images', blank=True)
    book = models.FileField(upload_to='e_library/pdfs', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
