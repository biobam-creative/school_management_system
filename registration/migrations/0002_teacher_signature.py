# Generated by Django 3.1.2 on 2020-10-18 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='signature',
            field=models.ImageField(blank=True, upload_to='registration/images'),
        ),
    ]
