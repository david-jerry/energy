# Generated by Django 3.2.12 on 2022-07-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0004_services_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticeboard',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
