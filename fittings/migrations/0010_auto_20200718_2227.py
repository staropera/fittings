# Generated by Django 2.2.14 on 2020-07-18 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('fittings', '0009_auto_20200605_2117'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UniCategory',
            new_name='Category',
        ),
    ]
