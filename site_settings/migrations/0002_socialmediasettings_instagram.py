# Generated by Django 3.0.4 on 2020-06-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediasettings',
            name='instagram',
            field=models.URLField(blank=True, help_text='Instagram URL', null=True),
        ),
    ]
