from mtaube.settings.base import *

try:
    from mtaube.settings.secret import *
except ImportError:
    pass


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

AWS_STORAGE_BUCKET_NAME = 'storage.staging.mtaube.com'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME


# Sites / Flatpages
# https://docs.djangoproject.com/en/1.8/ref/contrib/flatpages/

SITE_ID = 2
