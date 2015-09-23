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

"""Modular settings loader, primarily useful for multi-environment settings.

Values are read from the module specified by DJANGO_SETTINGS_MODULE and ENV
environment variables. All environment-specific modules should import base
settings first.

For example, to use dev.py as the settings module:

DJANGO_SETTINGS_MODULE='mtaube.settings'
DJANGO_ENV='dev'

For more information on this topic, see:
http://www.mtaube.com/words/modular-django-settings/
https://code.djangoproject.com/wiki/SplitSettings
https://code.djangoproject.com/wiki/SplitSettings#DevelopmentMachineDependantSettingsConfiguration
"""

import os


mod = __import__(
    os.environ['DJANGO_ENV'],
    globals(),
    locals(),
    ['settings']
)

for setting in dir(mod):
    if setting.isupper():
        locals()[setting] = getattr(mod, setting)
