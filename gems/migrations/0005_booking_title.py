# Generated by Django 3.2.23 on 2023-11-30 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gems', '0004_auto_20231127_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='title',
            field=models.CharField(default='Default Title', max_length=200),
        ),
    ]
