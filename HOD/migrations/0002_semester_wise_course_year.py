# Generated by Django 2.1.4 on 2019-07-11 14:11

import HOD.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOD', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester_wise_course',
            name='year',
            field=models.CharField(default=HOD.models.this_year, max_length=4),
        ),
    ]
