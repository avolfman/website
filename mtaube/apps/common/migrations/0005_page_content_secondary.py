# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20150825_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content_secondary',
            field=models.TextField(blank=True),
        ),
    ]
