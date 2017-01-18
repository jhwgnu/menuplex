# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20170118_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='school_url',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
