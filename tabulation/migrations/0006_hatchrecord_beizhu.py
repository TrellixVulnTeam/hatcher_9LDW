# Generated by Django 2.2.3 on 2020-05-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabulation', '0005_auto_20200521_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='hatchrecord',
            name='beizhu',
            field=models.TextField(blank=True, max_length=3200, null=True, verbose_name='备注'),
        ),
    ]
