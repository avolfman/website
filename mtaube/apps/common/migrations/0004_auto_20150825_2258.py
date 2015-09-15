# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_remove_page_template_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='media_panel_default',
            field=models.ForeignKey(related_name='common_page_panel', blank=True, to='common.MediaPanel', null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='media_panels',
            field=models.ManyToManyField(related_name='common_page_panels', to='common.MediaPanel', blank=True),
        ),
    ]
