# Generated by Django 2.2.12 on 2020-08-15 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fittings', '0011_auto_20200815_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_id', models.BigIntegerField()),
                ('type_name', models.CharField(max_length=500)),
            ],
            options={
                'default_permissions': (),
            },
        ),
    ]