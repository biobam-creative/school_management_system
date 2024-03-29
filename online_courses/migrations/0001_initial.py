# Generated by Django 3.1.2 on 2020-10-18 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('course_classs', models.CharField(choices=[('JSS1', 'JSS1'), ('JSS2', 'JSS2'), ('JSS3', 'JSS3'), ('SSS1', 'SSS1'), ('SSS2', 'SSS2'), ('SSS3', 'SSS3')], max_length=255)),
                ('subject', models.CharField(choices=[('English', 'English'), ('Mathematics', 'Mathematics'), ('Agricultural Science', 'Agricultural Science'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Literature-In-English', 'Literature-In-English'), ('Commerce', 'Commerce'), ('Economics', 'Economics')], max_length=255)),
                ('thumb_nail', models.ImageField(upload_to='online_courses/images')),
                ('url', models.URLField(blank=True)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('video', models.FileField(blank=True, upload_to='online_courses/videos')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_courses.category')),
            ],
        ),
    ]
