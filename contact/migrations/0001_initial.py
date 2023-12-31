# Generated by Django 3.2.20 on 2023-08-21 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(default='', max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]
