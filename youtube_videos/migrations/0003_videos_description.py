# Generated by Django 3.2.4 on 2021-12-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_videos', '0002_auto_20211219_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]