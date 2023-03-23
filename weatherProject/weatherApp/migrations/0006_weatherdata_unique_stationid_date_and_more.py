# Generated by Django 4.1.1 on 2023-03-23 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0005_delete_weatherdataall'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='weatherdata',
            constraint=models.UniqueConstraint(fields=('stationID', 'date'), name='unique_stationID_date'),
        ),
        migrations.AddConstraint(
            model_name='weatherlog',
            constraint=models.UniqueConstraint(fields=('stationID',), name='unique_stationID'),
        ),
    ]