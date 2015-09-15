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

from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def is_active(request, view_name):
    """
    Checks whether the current request path resolves to view_name.

    Args:
        request: (HttpRequest) instance
        view_name: (string) the view name to reverse

    Returns:
        (string) 'is-active' or ''
    """
    if reverse(view_name) == request.path:
        return 'is-active'
    return ''


@register.simple_tag
def is_active_prefix(request, view_name):
    """
    Checks whether the current request path prefix resolves to view_name.

    Args:
        request: (HttpRequest) instance
        view_name: (string) the view name to reverse

    Returns:
        (string) 'is-activePrefix' or ''
    """
    path = reverse(view_name)

    if path in request.path and path != request.path:
        return 'is-activePrefix'
    return ''
