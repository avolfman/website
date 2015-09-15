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

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from mtaube.apps.common.models import PageAbstract


class Post(PageAbstract):
    date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    color = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'slug': self.slug})
