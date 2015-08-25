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
from mtaube.apps.portfolio.models import Project


def index(request):
    """View used to render portfolio page.

    Args:
        request: (HttpRequest) instance

    Returns:
        (HttpResponse) instance
    """
    page = get_object_or_404(Page, url=request.path)
    projects = Project.objects.all()

    return render(request, 'page/portfolio/index.html', {
        'page': page,
        'projects': projects
    })


def project(request, slug):
    """View used to render project pages.

    Args:
        request: (HttpRequest) instance
        slug: (string) slug to query Project model

    Returns:
        (HttpResponse) instance
    """
    page = get_object_or_404(Project, slug=slug)

    return render(request, 'page/default.html', {'page': page})
