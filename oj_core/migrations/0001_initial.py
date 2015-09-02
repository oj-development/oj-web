# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('background', models.TextField()),
                ('description', models.TextField()),
                ('input', models.TextField()),
                ('output', models.TextField()),
                ('sample_input', models.TextField()),
                ('sample_output', models.TextField()),
                ('time_limitation', models.TextField()),
                ('hint', models.TextField()),
                ('source', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='problem',
            field=models.ForeignKey(to='oj_core.Problem'),
        ),
    ]
