# Generated by Django 3.2.12 on 2022-07-29 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_auto_20220729_1844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casestudies',
            options={'managed': True, 'ordering': ['-published'], 'verbose_name': 'Case Study', 'verbose_name_plural': 'Case Studies'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'managed': True, 'ordering': ['-created'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'managed': True, 'ordering': ['-published'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'managed': True, 'ordering': ['-created'], 'verbose_name': 'News Letter', 'verbose_name_plural': 'News Letters'},
        ),
        migrations.RemoveField(
            model_name='casestudies',
            name='category',
        ),
        migrations.AddField(
            model_name='casestudies',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='newsletter.category'),
        ),
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='newsletter.category'),
        ),
    ]
