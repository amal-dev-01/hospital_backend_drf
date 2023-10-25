# Generated by Django 4.2.6 on 2023-10-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0004_alter_userdetails_is_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='number',
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
    ]
