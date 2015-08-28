# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_thumbnail_font_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thumbnail_bg_color',
            new_name='color',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thumbnail_font_color',
        ),
        migrations.AddField(
            model_name='post',
            name='content_secondary',
            field=models.TextField(blank=True),
        ),
    ]
