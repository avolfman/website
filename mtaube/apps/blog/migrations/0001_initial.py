# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('meta_title', models.CharField(max_length=255, blank=True)),
                ('meta_keywords', models.CharField(max_length=255, blank=True)),
                ('meta_description', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
