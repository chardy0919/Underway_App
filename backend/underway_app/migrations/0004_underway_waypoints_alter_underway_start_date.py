# Generated by Django 4.2.7 on 2023-12-07 15:17

import datetime
import django.core.validators
from django.db import migrations, models
import underway_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('waypoint_app', '0001_initial'),
        ('underway_app', '0003_underway_crew_alter_underway_start_date_delete_crew'),
    ]

    operations = [
        migrations.AddField(
            model_name='underway',
            name='waypoints',
            field=models.ManyToManyField(to='waypoint_app.waypoint'),
        ),
        migrations.AlterField(
            model_name='underway',
            name='start_date',
            field=models.DateField(error_messages='invalid start date', validators=[underway_app.validators.validate_future_date, django.core.validators.MinValueValidator(limit_value=datetime.date(2023, 12, 7))]),
        ),
    ]
