# Generated by Django 3.2.23 on 2023-12-15 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gems', '0011_remove_post_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.TextField(blank=True),
        ),
    ]
