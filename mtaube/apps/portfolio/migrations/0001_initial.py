# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('meta_title', models.CharField(max_length=255, blank=True)),
                ('meta_keywords', models.CharField(max_length=255, blank=True)),
                ('meta_description', models.TextField(blank=True)),
                ('client_name', models.CharField(max_length=255, blank=True)),
                ('thumbnail', models.ImageField(upload_to=b'projects', blank=True)),
                ('thumbnail_bg_color', models.CharField(max_length=255, blank=True)),
                ('slug', models.SlugField(max_length=255)),
                ('is_locked', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('github_link', models.URLField(max_length=255, blank=True)),
                ('order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
