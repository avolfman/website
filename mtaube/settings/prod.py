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

"""Django settings for the staging environment.

Inherits the base settings and staging-specific secret settings. Used as
DJANGO_SETTINGS_MODULE whenever:

DJANGO_ENV='prod'
"""

from mtaube.settings.base import *

try:
    from mtaube.settings.secret import *
except ImportError:
    pass


# General Settings

ALLOWED_HOSTS = ['mtaube.com', 'www.mtaube.com']

DEBUG = False

HOSTS = ['ubuntu@54.153.8.86']

PREPEND_WWW = True

VIRTUALENV_NAME = 'lacy_prod'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

AWS_S3_CUSTOM_DOMAIN = 'storage.mtaube.com'
AWS_STORAGE_BUCKET_NAME = 'storage.mtaube.com'

DEFAULT_FILE_STORAGE = 'mtaube.apps.common.storages.MediaS3BotoStorage'
STATICFILES_STORAGE = 'mtaube.apps.common.storages.StaticCachedS3BotoStorage'

S3_URL = 'http://storage.mtaube.com'
STATIC_URL = '%s/static/' % S3_URL
MEDIA_URL = '%s/media/' % S3_URL
