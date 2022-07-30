# Generated by Django 3.2.12 on 2022-07-28 12:12

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import stdimage.models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('published', models.DateField(default=django.utils.timezone.now)),
                ('content', tinymce.models.HTMLField()),
                ('image', stdimage.models.StdImageField(blank=True, upload_to='news')),
                ('draft', models.BooleanField(default=False)),
                ('can_comment', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(blank=True, to='newsletter.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
