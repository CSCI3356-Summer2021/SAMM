# Generated by Django 3.2.4 on 2021-07-01 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_alter_userreport_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagereport',
            name='username',
            field=models.CharField(default='{{request.post.author}}', max_length=200, null=True),
        ),
    ]