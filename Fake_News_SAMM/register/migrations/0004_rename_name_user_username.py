# Generated by Django 3.2.4 on 2021-06-23 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_user_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]