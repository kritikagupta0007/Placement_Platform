# Generated by Django 3.1.4 on 2022-02-09 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_jobform_last_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobform',
            old_name='statue',
            new_name='status',
        ),
    ]
