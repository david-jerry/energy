# Generated by Django 3.2.12 on 2022-07-28 12:12

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0008_auto_20220724_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('logo', stdimage.models.StdImageField(upload_to='certificate/image/')),
                ('certificate', stdimage.models.StdImageField(upload_to='certificate/image/')),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificates',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('logo', stdimage.models.StdImageField(upload_to='membership/image/')),
                ('certificate', stdimage.models.StdImageField(upload_to='membership/image/')),
            ],
            options={
                'verbose_name': 'Membership',
                'verbose_name_plural': 'Memberships',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='services',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='slider',
            name='caption1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='slider',
            name='caption2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='slider',
            name='caption3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='comment',
            field=models.CharField(max_length=700),
        ),
    ]
