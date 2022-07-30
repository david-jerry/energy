# Generated by Django 3.2.12 on 2022-07-22 13:29

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('details', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('slider1', stdimage.models.StdImageField(blank=True, upload_to='home/slider')),
                ('slider2', stdimage.models.StdImageField(blank=True, upload_to='home/slider')),
                ('slider3', stdimage.models.StdImageField(blank=True, upload_to='home/slider')),
                ('title1', models.CharField(blank=True, max_length=250)),
                ('title2', models.CharField(blank=True, max_length=250)),
                ('title3', models.CharField(blank=True, max_length=250)),
                ('caption1', models.TextField()),
                ('caption2', models.TextField()),
                ('caption3', models.TextField()),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='faq',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
