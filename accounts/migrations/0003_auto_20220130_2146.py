# Generated by Django 3.1.4 on 2022-01-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220130_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='btech_branch',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(default='', max_length=6),
        ),
    ]
