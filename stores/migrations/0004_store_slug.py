# Generated by Django 2.0.7 on 2018-10-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_remove_store_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
