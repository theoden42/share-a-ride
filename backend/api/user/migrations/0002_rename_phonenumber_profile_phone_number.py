# Generated by Django 4.2 on 2024-05-22 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='PhoneNumber',
            new_name='phone_number',
        ),
    ]
