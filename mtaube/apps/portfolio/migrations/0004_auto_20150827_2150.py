# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project_thumbnail_font_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='thumbnail_bg_color',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='thumbnail',
            new_name='logo',
        ),
        migrations.RemoveField(
            model_name='project',
            name='thumbnail_font_color',
        ),
        migrations.AddField(
            model_name='project',
            name='content_secondary',
            field=models.TextField(blank=True),
        ),
    ]
