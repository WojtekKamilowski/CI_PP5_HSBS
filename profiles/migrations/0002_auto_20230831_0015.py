# Generated by Django 3.2.20 on 2023-08-30 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address1',
            new_name='default_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address2',
            new_name='default_address2',
        ),
    ]