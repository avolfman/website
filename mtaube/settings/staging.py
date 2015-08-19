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
