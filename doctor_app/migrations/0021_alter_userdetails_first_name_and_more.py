# Generated by Django 4.2.6 on 2023-11-01 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0020_alter_doctorprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='first_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='last_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
