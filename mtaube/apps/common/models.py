# Copyright 2015 Matt Taube
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class MediaPanel(models.Model):
    bg_color = models.CharField(max_length=255, blank=True)
    bg_image = models.ImageField(upload_to='panels', blank=True)
    id_target = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.id_target


@python_2_unicode_compatible
class PageAbstract(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    content_secondary = models.TextField(blank=True)
    media_panels = models.ManyToManyField(
        MediaPanel,
        related_name='%(app_label)s_%(class)s_panels',
        blank=True
    )
    media_panel_default = models.ForeignKey(
        MediaPanel,
        related_name='%(app_label)s_%(class)s_panel',
        blank=True,
        null=True
    )

    meta_title = models.CharField(max_length=255, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Page(PageAbstract):
    url = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return '%s - %s' % (self.title, self.url)
