# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-19 10:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastpostid',
            name='postdt',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 19, 10, 12, 28, 516921), verbose_name='DatetimeCommit'),
        ),
    ]
