# Generated by Django 5.2.3 on 2025-06-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FootZonePlusApp', '0006_remove_match_lieu'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='billets/'),
        ),
    ]
