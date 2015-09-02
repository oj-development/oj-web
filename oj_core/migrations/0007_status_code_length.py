# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj_core', '0006_auto_20150902_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='code_length',
            field=models.PositiveIntegerField(default=123),
            preserve_default=False,
        ),
    ]
