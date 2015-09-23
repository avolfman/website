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

"""Django context processors for mtaube project."""

from mtaube.apps.common.conf import GOOGLE_ANALYTICS_CODE
from mtaube.apps.common.conf import MODERNIZR_BUILD
from mtaube.apps.common.conf import REQUIREJS_BUILD


def google(request):
    """Adds Google-related context variables to the context."""

    return {
        'GOOGLE_ANALYTICS_CODE': GOOGLE_ANALYTICS_CODE
    }


def modernizr(request):
    """Adds Modernizr-related context variables to the context."""
    path = 'js/lib/modernizr.js'

    if MODERNIZR_BUILD:
        path = 'built/' + path

    return {
        'MODERNIZR_BUILD': MODERNIZR_BUILD,
        'MODERNIZR_PATH': path
    }


def requirejs(request):
    """Adds RequireJS-related context variables to the context."""

    return {
        'REQUIREJS_BUILD': REQUIREJS_BUILD
    }
