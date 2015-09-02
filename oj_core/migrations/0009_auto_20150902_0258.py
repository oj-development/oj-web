# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oj_core', '0008_userstatus_solved_problems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='memory',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='status',
            name='result',
            field=models.PositiveSmallIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='status',
            name='score',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='status',
            name='time',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='status',
            name='user',
            field=models.ForeignKey(to='oj_core.UserStatus', null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
