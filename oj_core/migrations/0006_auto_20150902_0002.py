# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj_core', '0005_auto_20150901_2337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['-submit_time'], 'verbose_name_plural': 'statuses'},
        ),
        migrations.AlterModelOptions(
            name='userstatus',
            options={'ordering': ['user_id'], 'verbose_name_plural': 'user statuses'},
        ),
    ]
