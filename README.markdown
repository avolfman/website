# [mtaube.com](http://www.mtaube.com)

## Installation

### Prerequisites

- Python
- [pip](https://pip.pypa.io/en/stable/installing.html)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)

### Main

Using virtualenv and virtualenvwrapper is highly recommended. The virtualenv can be named anything (VIRTUALENV_NAME).

1. Create new virtualenv

    ```
    mkproject VIRTUALENV_NAME
    ```

2. Clone the repo into the new virtualenv dir

    ```
    git clone git@github.com:mtaube/mtaube.com.git .
    ```

3. Install the [Python required packages](requirements.txt)

    ```
    pip install -r requirements.txt
    ```

4. Configure Django settings

    Settings can be configured on a per-environment basis. There has been [much discussion](https://code.djangoproject.com/wiki/SplitSettings) on the best way to do it, see the [settings module initialization](mtaube/settings/__init__.py) for this project's implementation and required environment variables. It is recommended to set and unset the variables in the ``activate`` hook provided by virtualenv.

    See [Django's settings documentation](https://docs.djangoproject.com/en/1.8/ref/settings/) for all possible configurations.

5. Initialize the database tables

    ```
    python manage.py migrate
    ```