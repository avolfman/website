# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='template_name',
            field=models.CharField(help_text=b"Example: 'flatpages/contact_page.html'", max_length=255, blank=True),
        ),
    ]
