# Generated by Django 2.2.4 on 2020-11-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='isFriend',
            field=models.BooleanField(default=False),
        ),
    ]
