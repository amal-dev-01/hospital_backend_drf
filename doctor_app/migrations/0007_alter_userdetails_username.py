# Generated by Django 4.2.6 on 2023-10-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0006_alter_userdetails_is_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
