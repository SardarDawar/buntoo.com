# Generated by Django 2.2.4 on 2020-07-03 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trading', '0010_auto_20200703_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend_list',
            name='friend_name',
        ),
        migrations.AddField(
            model_name='friend_list',
            name='friend_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='list', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
