# Generated by Django 4.1.6 on 2023-05-30 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_user_profile_image"),
    ]

    operations = [
        migrations.DeleteModel(name="Profile",),
    ]
