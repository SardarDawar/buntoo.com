# Generated by Django 2.2.4 on 2020-07-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0013_advert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='img',
            field=models.ImageField(blank=True, upload_to='ad_images'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='video',
            field=models.FileField(blank=True, upload_to='ad_videos'),
        ),
    ]
