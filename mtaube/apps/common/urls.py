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

from django.conf.urls import url

from mtaube.apps.common.views import PageView


urlpatterns = [
    url(
        r'^$',
        PageView.as_view(template_name='page/home.html'),
        {'slug': 'home'},
        name='home'
    ),
    url(
        r'^contact/$',
        PageView.as_view(template_name='page/contact.html'),
        {'slug': 'contact'},
        name='contact'
    ),
    url(
        r'^profile/$',
        PageView.as_view(),
        {'slug': 'profile'},
        name='profile'
    ),
]
