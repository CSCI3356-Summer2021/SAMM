# Generated by Django 3.2.2 on 2021-06-30 17:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_alter_user_bio'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_id', to='register.user', verbose_name='User_RELA'),
            preserve_default=False,
        ),
    ]
