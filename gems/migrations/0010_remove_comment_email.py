# Generated by Django 3.2.23 on 2023-12-11 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gems', '0009_booking_number_of_viewers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]