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

from django.shortcuts import get_object_or_404, render

from mtaube.apps.common.models import Page


DEFAULT_TEMPLATE = 'page/default.html'


def page(request, url):
    """View used to render flat pages (Home, Contact, etc.).

    Args:
        request: (HttpRequest) instance
        url: (string) URL pattern to query Page model

    Returns:
        (HttpResponse) instance
    """
    page = get_object_or_404(Page, url=url)

    if page.template_name:
        template = page.template_name
    else:
        template = DEFAULT_TEMPLATE

    return render(request, template, {'page': page})
