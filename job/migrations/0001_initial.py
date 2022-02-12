# Generated by Django 3.1.4 on 2022-02-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='', max_length=50)),
                ('profile', models.CharField(default='', max_length=30)),
                ('package', models.IntegerField(default=0)),
                ('eligibility', models.CharField(default='', max_length=100)),
                ('drive_date', models.CharField(default='', max_length=15)),
                ('statue', models.CharField(default='', max_length=15)),
            ],
        ),
    ]