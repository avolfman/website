# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20150829_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote', models.TextField()),
                ('author', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='mediapanel',
            name='quotes',
            field=models.ManyToManyField(to='common.Quote', blank=True),
        ),
    ]
