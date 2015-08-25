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

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from mtaube.apps.common.models import Page


DEFAULT_PAGE_TEMPLATE = 'page/default.html'


class PageView(DetailView):
    """View used to render flat pages (Home, Contact, etc.)."""
    model = Page
    template_name = DEFAULT_PAGE_TEMPLATE

    def get_object(self):
        return get_object_or_404(Page, url=self.request.path)


class PageListView(ListView):
    """View used to render list pages with associated flat page object."""

    def get_context_data(self, **kwargs):
        context = super(PageListView, self).get_context_data(**kwargs)

        context['page'] = get_object_or_404(Page, url=self.request.path)

        return context
