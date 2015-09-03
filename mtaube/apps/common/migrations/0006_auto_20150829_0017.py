# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_page_content_secondary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='url',
        ),
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
