# [mtaube.com](http://www.mtaube.com) v1.0.2

For an overview of the project architecture and tools used, check out [my blog post](http://www.mtaube.com/words/mtaubecom-v100/) about it.

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

3. Install the [Python required packages](requirements.txt) and [Node required packages](requirements--node.txt)

    ```
    pip install -r requirements.txt

    nodeenv --python-virtualenv --requirements=requirements--node.txt
    npm install
    ```

4. Configure Django settings

    Settings can be configured on a per-environment basis. Check out [my blog post](http://www.mtaube.com/words/modular-django-settings/) about it to see how this project's setting package works.

    See [Django's settings documentation](https://docs.djangoproject.com/en/1.8/ref/settings/) for all possible configurations.

5. Initialize the database tables (make sure database exists and Django database settings are correct)

    ```
    python manage.py migrate
    ```

## Development

- Run Django's development server

    ```
    python manage.py runserver
    ```

- Automatically compile LESS files on save

    ```
    grunt watch
    ```

## Deployment

All deployment-related tasks are handled using [Fabric](http://docs.fabfile.org/en/1.8/). See the [fabfile](fabfile.py) for the predefined commands.

- To deploy an update to the staging or production environments

    ```
    fab -R staging deploy
    ```
