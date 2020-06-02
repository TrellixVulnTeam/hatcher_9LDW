# Generated by Django 2.2.3 on 2020-05-21 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabulation', '0004_auto_20200521_0757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hatchdetail',
            old_name='break_eggs',
            new_name='cipodanshu',
        ),
        migrations.RenameField(
            model_name='hatchdetail',
            old_name='m_miao',
            new_name='gongmiao',
        ),
        migrations.RenameField(
            model_name='hatchdetail',
            old_name='all_miao',
            new_name='heji',
        ),
        migrations.RenameField(
            model_name='hatchdetail',
            old_name='fix_miao',
            new_name='hunhemiao',
        ),
        migrations.RenameField(
            model_name='hatchdetail',
            old_name='live_eggs',
            new_name='huojingdanshu',
        ),
        migrations.RenameField(
            model_name='hatchdetail',
            old_name='number_cases',
            new_name='jianshu',
        ),
        migrations.RenameField(
            model_name='hatchdetail',
            old_name='f_miao',
            new_name='mumiao',
        ),
        migrations.RenameField(
            model_name='hatchdetail',
            old_name='varieties',
            new_name='pinzhong',
        ),
        migrations.RenameField(
            model_name='hatchdetail',
            old_name='fertilization_rate',
            new_name='shoujinglv',
        ),
        migrations.RenameField(
            model_name='hatchdetail',
            old_name='shoujing_rate',
            new_name='shuojingdanchumiaol',
        ),
        migrations.RenameField(
            model_name='hatchdetail',
            old_name='dead_eggs',
            new_name='wujingdanshu',
        ),
        migrations.RenameField(
            model_name='hatchdetail',
            old_name='zongdan_rate',
            new_name='zhongdanchumiaolv',
        ),
        migrations.RenameField(
            model_name='hatchdetail',
            old_name='all_number',
            new_name='zhuangjidanshu',
        ),
        migrations.AddField(
            model_name='hatchdetail',
            name='maodanshu',
            field=models.IntegerField(blank=True, null=True, verbose_name='毛蛋数'),
        ),
    ]
