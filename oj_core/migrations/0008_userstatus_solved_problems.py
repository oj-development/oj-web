# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj_core', '0007_status_code_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstatus',
            name='solved_problems',
            field=models.ManyToManyField(to='oj_core.Problem'),
        ),
    ]
