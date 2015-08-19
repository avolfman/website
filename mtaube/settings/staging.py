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

DJANGO_ENV='staging'
"""

from mtaube.settings.base import *

try:
    from mtaube.settings.secret import *
except ImportError:
    pass


# General Settings

DEBUG = True

HOSTS = ['ubuntu@54.153.8.86']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

AWS_STORAGE_BUCKET_NAME = 'storage.staging.mtaube.com'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATIC_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME


# Sites / Flatpages
# https://docs.djangoproject.com/en/1.8/ref/contrib/flatpages/

SITE_ID = 2
