"""Modular settings loader, primarily useful for multi-environment settings.

Values are read from the module specified by DJANGO_SETTINGS_MODULE and ENV
environment variables. All environment-specific modules should import base
settings first.

For example, to use dev.py as the settings module:
DJANGO_SETTINGS_MODULE='mtaube.settings'
ENV='dev'

For more information on this topic, see
https://code.djangoproject.com/wiki/SplitSettings
https://code.djangoproject.com/wiki/SplitSettings#DevelopmentMachineDependantSettingsConfiguration
"""

import os


mod = __import__(
    os.environ['ENV'],
    globals(),
    locals(),
    ['settings']
)

for setting in dir(mod):
    if setting.isupper():
        locals()[setting] = getattr(mod, setting)
