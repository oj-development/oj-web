# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj_core', '0003_auto_20150826_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='data',
        ),
        migrations.AddField(
            model_name='data',
            name='data_hash',
            field=models.CharField(max_length=32, default='d41d8cd98f00b204e9800998ecf8427e'),
            preserve_default=False,
        ),
    ]
