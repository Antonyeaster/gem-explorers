# Generated by Django 3.2.23 on 2023-12-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gems', '0008_timestamp_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='number_of_viewers',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
