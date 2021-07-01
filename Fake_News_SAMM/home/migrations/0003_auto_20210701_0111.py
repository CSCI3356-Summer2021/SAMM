# Generated by Django 3.2.2 on 2021-06-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_twitter_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitter',
            name='user',
        ),
        migrations.AddField(
            model_name='twitter',
            name='avatar',
            field=models.CharField(default='', max_length=64, verbose_name='profile_picture'),
        ),
        migrations.AlterField(
            model_name='twitter',
            name='username',
            field=models.CharField(max_length=64, verbose_name='username'),
        ),
    ]
