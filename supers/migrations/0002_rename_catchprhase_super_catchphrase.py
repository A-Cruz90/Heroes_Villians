# Generated by Django 4.1.3 on 2022-12-08 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super',
            old_name='catchprhase',
            new_name='catchphrase',
        ),
    ]