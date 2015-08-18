from mtaube.settings.base import *

try:
    from mtaube.settings.secret import *
except ImportError:
    pass


# Sites / Flatpages
# https://docs.djangoproject.com/en/1.8/ref/contrib/flatpages/

SITE_ID = 2
