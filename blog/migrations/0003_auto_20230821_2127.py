# Generated by Django 3.2.20 on 2023-08-21 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230821_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_image_url',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]