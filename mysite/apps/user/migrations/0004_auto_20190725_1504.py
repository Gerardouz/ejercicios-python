# Generated by Django 2.2.3 on 2019-07-25 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190722_1545'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Data',
            new_name='User',
        ),
    ]
