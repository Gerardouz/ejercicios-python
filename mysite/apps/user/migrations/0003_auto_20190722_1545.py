# Generated by Django 2.2.3 on 2019-07-22 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190722_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='data_dueño_id',
            new_name='dueño',
        ),
    ]
