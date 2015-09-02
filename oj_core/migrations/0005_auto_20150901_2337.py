# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj_core', '0004_auto_20150827_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('runid', models.CharField(max_length=32)),
                ('score', models.PositiveSmallIntegerField()),
                ('result', models.PositiveSmallIntegerField()),
                ('memory', models.PositiveIntegerField()),
                ('time', models.FloatField()),
                ('language', models.CharField(max_length=7, choices=[('pas', 'Pascal'), ('c', 'C'), ('cpp', 'C++')])),
                ('code', models.TextField()),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('user_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('submit', models.PositiveIntegerField(default=0)),
                ('ac', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['user_id'],
            },
        ),
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ['name']},
        ),
        migrations.AlterUniqueTogether(
            name='problem',
            unique_together=set([('name', 'description')]),
        ),
        migrations.AddField(
            model_name='status',
            name='problem',
            field=models.ForeignKey(to='oj_core.Problem'),
        ),
        migrations.AddField(
            model_name='status',
            name='user',
            field=models.ForeignKey(to='oj_core.UserStatus'),
        ),
    ]
