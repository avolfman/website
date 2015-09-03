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

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from mtaube.apps.common.models import Page

DEFAULT_PAGE_TEMPLATE = 'page/default.html'


class JsonResponseMixin(object):
    """Mixin used to render a JSON response.

    Credit: https://docs.djangoproject.com/en/1.8/topics/class-based-views/
            /mixins/#jsonresponsemixin-example
    """

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        """Returns an object that will be serialized as JSON by json.dumps().

        When overriding, ensure arbitrary objects can be serialized as JSON.
        """
        return context


class HybridPageMixin(JsonResponseMixin):
    """Mixin used to render either a HTML or JSON response.

    If request is AJAX, a JSON response is returned. Otherwise, an HTML
    response is returned.

    Credit: https://docs.djangoproject.com/en/1.8/topics/class-based-views/
            /mixins/#jsonresponsemixin-example
    """

    def render_to_response(self, context):
        """Checks whether request is AJAX and renders appropriate response."""
        if self.request.is_ajax():
            return self.render_to_json_response(context)
        else:
            context['base_template'] = 'base.html'

            return super(HybridPageMixin, self).render_to_response(context)

    def get_data(self, context):
        """Adds page HTML and title to JSON response data."""
        page = context['page']
        template_names = self.get_template_names()
        context_instance = RequestContext(self.request)

        context['base_template'] = 'base_content.html'
        html = render_to_string(
            template_names,
            context,
            context_instance
        )

        return {
            'title': page.title,
            'html': html
        }


class PageView(HybridPageMixin, DetailView):
    """View used to render flat pages (Home, Contact, etc.)."""
    model = Page
    template_name = DEFAULT_PAGE_TEMPLATE


class PageListView(HybridPageMixin, ListView):
    """View used to render list pages with associated flat page object."""

    def get_context_data(self, **kwargs):
        context = super(PageListView, self).get_context_data(**kwargs)

        context['page'] = get_object_or_404(
            Page,
            slug=self.kwargs['page_slug']
        )

        return context
