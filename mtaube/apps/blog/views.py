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

from django.views.generic.detail import DetailView

from mtaube.apps.common.views import PageListView
from mtaube.apps.blog.models import Post


class IndexView(PageListView):
    """View used to render blog index page."""
    model = Post
    template_name = 'page/blog/index.html'
    context_object_name = 'posts'


class PostView(DetailView):
    """View used to render blog post pages."""
    model = Post
    template_name = 'page/blog/post.html'
    context_object_name = 'page'
