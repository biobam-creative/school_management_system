# Generated by Django 3.1.2 on 2020-10-18 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('teachers', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('First Term', 'First Term'), ('Second Term', 'Second Term'), ('Third Term', 'Third Term')], max_length=20)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.session')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priviledge', models.BooleanField(default=True)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('religion', models.CharField(max_length=50)),
                ('joining_date', models.DateField()),
                ('class_taught', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=255)),
                ('picture', models.ImageField(blank=True, default='registration/images/0011.jpg', upload_to='registration/images')),
                ('subjects_taught', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.subject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10)),
                ('class_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('religion', models.CharField(max_length=255)),
                ('section', models.CharField(max_length=255)),
                ('father_occupation', models.CharField(max_length=255)),
                ('admission_date', models.DateField()),
                ('date_of_birth', models.DateField()),
                ('picture', models.ImageField(default='registration/images/0011.jpg', upload_to='registration/images')),
                ('parent_contact', models.CharField(max_length=11)),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.studentclass')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
