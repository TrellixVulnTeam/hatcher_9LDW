# Generated by Django 2.2.3 on 2020-05-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabulation', '0002_auto_20200519_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hatchrecord',
            name='out_machine',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='出壳机'),
        ),
    ]
