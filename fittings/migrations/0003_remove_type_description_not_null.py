# Generated by Django 2.2.12 on 2020-05-11 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fittings', '0002_add_dgm_unique_constraints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='description',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
