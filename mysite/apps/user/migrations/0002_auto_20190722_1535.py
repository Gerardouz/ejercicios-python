# Generated by Django 2.2.3 on 2019-07-22 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'ordering': ['nombre'], 'verbose_name': 'Info', 'verbose_name_plural': 'Datos'},
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=100)),
                ('placa', models.IntegerField()),
                ('data_dueño_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Data')),
            ],
            options={
                'ordering': ['modelo'],
                'verbose_name_plural': 'Autos',
                'verbose_name': 'Auto',
            },
        ),
    ]
