# Generated by Django 4.1.1 on 2023-03-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0006_weatherdata_unique_stationid_date_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='weatherstatistics',
            constraint=models.UniqueConstraint(fields=('stationID', 'year'), name='unique_stationID_year'),
        ),
    ]