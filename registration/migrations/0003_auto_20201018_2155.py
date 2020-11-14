# Generated by Django 3.1.2 on 2020-10-18 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_teacher_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MR', max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='title',
            field=models.CharField(choices=[('MR', 'MR'), ('MRS', 'MRS'), ('CHIEF', 'CHIEF'), ('PASTOR', 'PASTOR'), ('REV', 'REV'), ('EVANG', 'EVANG'), ('DR', 'DR'), ('PROF', 'PROF')], default='MALE', max_length=20),
        ),
    ]