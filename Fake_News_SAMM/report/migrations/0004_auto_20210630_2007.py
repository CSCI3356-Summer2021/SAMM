# Generated by Django 3.2.4 on 2021-07-01 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20210630_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagereport',
            name='username',
            field=models.CharField(default='{{request.post.author}}', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='userreport',
            name='username',
            field=models.CharField(default='{{request.post.author}}', max_length=7, null=True),
        ),
    ]
