# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-27 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0004_auto_20180327_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='no_drop',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='no_grads',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='no_homework',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='no_tennent',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='no_viper',
            field=models.IntegerField(default=1),
        ),
    ]
