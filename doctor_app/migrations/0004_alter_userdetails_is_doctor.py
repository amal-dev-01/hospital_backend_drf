# Generated by Django 4.2.6 on 2023-10-23 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0003_alter_userdetails_is_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='is_doctor',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
