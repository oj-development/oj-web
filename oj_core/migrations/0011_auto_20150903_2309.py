# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj_core', '0010_auto_20150902_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='ac',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='problem',
            name='submit',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstatus',
            name='ac_problems',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstatus',
            name='submit_problems',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstatus',
            name='tried_problems',
            field=models.ManyToManyField(to='oj_core.Problem', related_name='tried_by'),
        ),
        migrations.AlterField(
            model_name='userstatus',
            name='solved_problems',
            field=models.ManyToManyField(to='oj_core.Problem', related_name='solved_by'),
        ),
    ]
