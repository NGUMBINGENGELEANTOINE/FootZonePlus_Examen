# Generated by Django 5.2.3 on 2025-06-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FootZonePlusApp', '0007_reservation_pdf_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apropos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('titre', models.CharField(max_length=200, null=True)),
                ('slogan', models.CharField(max_length=200, null=True)),
                ('contenus', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50, null=True)),
                ('telephone', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
