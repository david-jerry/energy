# Generated by Django 3.2.12 on 2022-07-30 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0008_auto_20220730_0613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='slug'),
        ),
    ]
