# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj_core', '0009_auto_20150902_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='runid',
            field=models.UUIDField(),
        ),
    ]
