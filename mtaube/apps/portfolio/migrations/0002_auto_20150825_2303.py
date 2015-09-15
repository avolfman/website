# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20150825_2258'),
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='media_panel_default',
            field=models.ForeignKey(related_name='portfolio_project_panel', blank=True, to='common.MediaPanel', null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='media_panels',
            field=models.ManyToManyField(related_name='portfolio_project_panels', to='common.MediaPanel', blank=True),
        ),
    ]
