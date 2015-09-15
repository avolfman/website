# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20150825_2258'),
        ('blog', '0002_auto_20150825_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='media_panel_default',
            field=models.ForeignKey(related_name='blog_post_panel', blank=True, to='common.MediaPanel', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='media_panels',
            field=models.ManyToManyField(related_name='blog_post_panels', to='common.MediaPanel', blank=True),
        ),
    ]
