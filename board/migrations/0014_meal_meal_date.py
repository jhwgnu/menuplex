# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_auto_20170207_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='meal_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 7, 7, 48, 24, 604262, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
