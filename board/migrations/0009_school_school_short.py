# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-26 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20170126_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='school_short',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
