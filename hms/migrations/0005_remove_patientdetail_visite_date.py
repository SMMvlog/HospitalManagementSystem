# Generated by Django 3.2.3 on 2021-05-21 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0004_auto_20210520_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdetail',
            name='visite_Date',
        ),
    ]
