# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20150825_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail_font_color',
            field=models.CharField(default=b'black', max_length=255, choices=[(b'black', b'Black'), (b'white', b'White')]),
        ),
    ]
