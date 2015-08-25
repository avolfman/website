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
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible

from mtaube.apps.common.models import PageAbstract


@python_2_unicode_compatible
class Project(PageAbstract):
    client_name = models.CharField(max_length=255, blank=True)
    github_link = models.URLField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_locked = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)
    slug = models.SlugField(max_length=255)
    thumbnail = models.ImageField(upload_to='projects', blank=True)
    thumbnail_bg_color = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            if self.client_name:
                self.slug = slugify(self.client_name)
            else:
                self.slug = slugify(self.title)

        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        if self.client_name:
            return self.client_name
        return self.title
