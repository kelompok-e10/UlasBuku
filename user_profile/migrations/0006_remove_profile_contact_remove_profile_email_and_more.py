# Generated by Django 4.2.6 on 2023-10-28 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_remove_profile_contact_phone_profile_contact_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
