# Generated by Django 3.2.4 on 2022-11-05 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20221016_0656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hometable',
            old_name='value1',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='hometable',
            name='value2',
        ),
    ]
