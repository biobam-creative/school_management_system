# Generated by Django 3.1.2 on 2020-11-12 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_term_school_fee'),
        ('finance', '0002_auto_20201112_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolFeeBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.PositiveIntegerField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.student')),
            ],
        ),
        migrations.DeleteModel(
            name='TermFee',
        ),
    ]
