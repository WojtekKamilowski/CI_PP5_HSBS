# Generated by Django 3.2.20 on 2023-07-26 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='abc', max_length=260),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(blank=True, max_length=260, null=True),
        ),
    ]
