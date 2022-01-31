# Generated by Django 3.1.4 on 2022-01-30 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='first_name',
        ),
        migrations.AddField(
            model_name='register',
            name='admission_number',
            field=models.CharField(default='0000000', max_length=9),
        ),
        migrations.AddField(
            model_name='register',
            name='btech_branch',
            field=models.CharField(default='Other', max_length=6),
        ),
        migrations.AddField(
            model_name='register',
            name='btech_percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='register',
            name='class_10th_percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='register',
            name='class_12th_percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='register',
            name='date_Of_Birth',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='register',
            name='email',
            field=models.EmailField(default='not define', max_length=30),
        ),
        migrations.AddField(
            model_name='register',
            name='full_name',
            field=models.CharField(default='NoName', max_length=30),
        ),
        migrations.AddField(
            model_name='register',
            name='gender',
            field=models.CharField(default='Not given', max_length=6),
        ),
        migrations.AddField(
            model_name='register',
            name='parents_phone_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(default='Not define', max_length=30),
        ),
        migrations.AddField(
            model_name='register',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='register',
            name='university_rollnumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='register',
            name='upload_Resume',
            field=models.FileField(default='Null', max_length=254, upload_to=None),
        ),
        migrations.AlterField(
            model_name='register',
            name='aadhar_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='register',
            name='father_name',
            field=models.CharField(default='No name', max_length=30),
        ),
        migrations.AlterField(
            model_name='register',
            name='mother_name',
            field=models.CharField(default='NoName', max_length=30),
        ),
    ]