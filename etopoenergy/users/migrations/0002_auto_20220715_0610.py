# Generated by Django 3.2.12 on 2022-07-15 05:10

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('countries_plus', '0005_auto_20160224_1804'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.ForeignKey(blank=True, default='NG', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='countries_plus.country'),
        ),
        migrations.AddField(
            model_name='user',
            name='dp',
            field=stdimage.models.StdImageField(blank=True, upload_to='user/dp'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, help_text='eg: 018276475673', max_length=17),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('STAFF', 'Staff'), ('CONTRATOR', 'Contractor'), ('CLIENT', 'Client'), ('INTERN', 'Intern'), ('ADMINISTRATION', 'Administration'), ('NOTYPE', 'No Type')], default='CLIENT', max_length=255, verbose_name='Permission Type'),
        ),
    ]
