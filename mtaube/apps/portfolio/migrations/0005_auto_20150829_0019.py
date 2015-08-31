# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20150827_2150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order']},
        ),
    ]
