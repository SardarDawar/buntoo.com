# Generated by Django 2.2.4 on 2020-11-03 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_isfriend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='isFriend',
        ),
    ]