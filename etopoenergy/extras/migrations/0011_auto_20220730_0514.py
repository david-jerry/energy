# Generated by Django 3.2.12 on 2022-07-30 04:14

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0010_auto_20220729_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('content', tinymce.models.HTMLField()),
            ],
            options={
                'verbose_name': 'Static Page',
                'verbose_name_plural': 'Static Pages',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='testimonials',
            name='company',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
