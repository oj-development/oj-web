# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='background',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='hint',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='input',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='output',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='sample_input',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='sample_output',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='source',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='time_limitation',
            field=models.TextField(blank=True),
        ),
    ]
