# Generated by Django 4.0.3 on 2022-04-07 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_bookmark_profiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='profiles',
        ),
        migrations.AddField(
            model_name='profile',
            name='bookmarks',
            field=models.ManyToManyField(to='main_app.bookmark'),
        ),
    ]
