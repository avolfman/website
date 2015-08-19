"""Fabric commands for mtaube project.

Roles are used to distinguish between the dev, staging, and prod environments.
The hosts for each environment are loaded from the appropriate settings file.

If a role is provided it is assumed to be the dev role and the virtualenv is
assumed to be already activated, otherwise the fab command wouldn't be
available. So the following two commands are the same:

fab -R dev clear_cache
fab clear_cache

If a role is provided the host's virtualenv is activated before the
command is run. Use the -R option to select the role, like:

fab -R staging deploy

Note that all Fabric command-line arguments are converted to strings, so we
must handle boolean arguments appropriately.
"""

from contextlib import contextmanager
from distutils.util import strtobool

from fabric.api import env
from fabric.api import local
from fabric.api import prefix
from fabric.api import run
from fabric.api import runs_once
from fabric.api import sudo
from fabric.api import task

from mtaube.settings import VIRTUALENV_NAME
from mtaube.settings.staging import HOSTS as HOSTS_STAGING


# General Settings

env.colorize_errors = True
env.roledefs = {
    'dev': [],
    'staging': {
        'hosts': HOSTS_STAGING
    },
}


# Virtualenv Management

@contextmanager
def virtualenv():
    """Prefix with the virtualenv's activate command"""
    with prefix('workon %s' % VIRTUALENV_NAME):
        yield


def _run(command):
    """Run command locally or remotely in the virtualenv

    Args:
        command: (string) command to execute.
    """
    if env.host_string and env.host_string != 'localhost':
        with virtualenv():
            run(command)
    else:
        local(command)


# Commands

@task
def bounce():
    """Restarts the Apache server."""
    sudo('service apache2 restart')


@task
def clear_cache():
    """Clears the cached .pyc files."""
    _run('find . -name "*.pyc" -exec rm -rf {} \;')


@runs_once
@task
def collectstatic():
    """Runs Django's collectstatic command."""
    _run('python manage.py collectstatic --noinput')


@task
def deploy(minor='True'):
    """Deploys an update.

    Args:
        minor: (boolean string) whether upgrade does not include new
            requirements or database migrations.
    """
    pull()

    if not strtobool(minor):
        install_requirements()
        migrate()

    collectstatic()
    bounce()


@task
def install_requirements():
    """Installs project requirements using pip."""
    _run('pip install -r requirements.txt')


@runs_once
@task
def migrate():
    """Runs Django's migrate command."""
    _run('python manage.py migrate --noinput')


@task
def pull():
    """Sync the Git repo with the remote."""
    _run('git pull')
