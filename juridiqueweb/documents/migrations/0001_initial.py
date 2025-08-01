# Generated by Django 5.2 on 2025-07-23 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('fichier', models.FileField(upload_to='documents/')),
                ('date_upload', models.DateTimeField(auto_now_add=True)),
                ('visible_par_client', models.BooleanField(default=True)),
                ('lié_au_dossier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.dossierjuridique')),
            ],
        ),
    ]
