# Generated by Django 3.1.4 on 2022-02-09 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobform',
            name='last_date',
            field=models.CharField(default='', max_length=15),
        ),
    ]
