# Generated by Django 3.2.3 on 2021-05-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0003_auto_20210520_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetail',
            name='Mobile_No',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='patientdetail',
            name='Mobile_No',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='patientdetail',
            name='visite_Date',
            field=models.DateTimeField(),
        ),
    ]
