# Generated by Django 4.2.23 on 2025-06-27 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='featured_image',
            new_name='profile_image',
        ),
    ]
