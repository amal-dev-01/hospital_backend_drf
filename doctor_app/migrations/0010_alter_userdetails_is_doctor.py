# Generated by Django 4.2.6 on 2023-10-25 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0009_alter_userprofile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
    ]