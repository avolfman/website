# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaPanel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_target', models.CharField(unique=True, max_length=255)),
                ('bg_color', models.CharField(max_length=255, blank=True)),
                ('bg_image', models.ImageField(upload_to=b'panels', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('meta_title', models.CharField(max_length=255, blank=True)),
                ('meta_keywords', models.CharField(max_length=255, blank=True)),
                ('meta_description', models.TextField(blank=True)),
                ('url', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
