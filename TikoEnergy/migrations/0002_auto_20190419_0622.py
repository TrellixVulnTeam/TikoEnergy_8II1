# Generated by Django 2.0.5 on 2019-04-19 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TikoEnergy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
