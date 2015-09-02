# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj_core', '0002_auto_20150821_0113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'ordering': ['problem'], 'verbose_name': 'datum', 'verbose_name_plural': 'data'},
        ),
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ['name'], 'verbose_name': 'problem', 'verbose_name_plural': 'problems'},
        ),
    ]
