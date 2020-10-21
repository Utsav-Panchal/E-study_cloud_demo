# Maintainable Django Design Pattern Architecture

Powered by [Django Circle](https://djangocircle.com/), Simple, easy to understand and maintainable django project architecture.

To start new django project, don't need to take care and research to setup basic process and installation process. All things will get here.

# Getting Started

## Features

- For Django 3.0
- Works with Python 3.7 or latest version
- Renders Django projects with 100% coverage all django concepts with base architecture and generic views.
- Rest API implementation using [Django Rest Framework](https://www.django-rest-framework.org/) support.
- Swagger API Documentation using [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/).
- [12-Factor](https://12factor.net/) based settings via [django-environ](https://django-environ.readthedocs.io/en/latest/)
- Optimized development and production settings
- Registration via [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- Comes with custom user model ready to go
- Optional basic ASGI setup for Websockets
- Customizable PostgreSQL version
- Default integration with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review

## Installation

**Clone the repo:**

```sh
git clone https://github.com/djangocircle/django-design-pattern-architecture.git
```

## Requirements

- Latest `Python 3.7` runtime environment.

  - To install python, just execute ready Linux shell script : [01-install-python3x.sh](setup_environments/01-install-python3x.sh)
  - This script will install all depedencies which require `Python` environment and `pip`.
  - By default it install `Python 3.7.5` version, if you want to upgrade version, you just need to change `VERSION` value from script and execute it.

  ```
    chmod +x setup_environments/
    sh setup_environments/01-install-python3x.sh
  ```

- `PostgreSQL`

  - To install postgres server in your Linux machine just execute: [02-install-postgresql.sh](setup_environments/02-install-postgresql.sh)
  - This script will install latest version of postgresql server and all dependencies which require to setup postgresql.

  ```
    sh setup_environments/02-install-postgresql.sh
  ```

- `Virtualenv`

  - To install virtualenv, execute shell script: [03-setup-virtualenv.sh](setup_environments/03-setup-virtualenv.sh)
  - This script will install virtual environment with default `Python 3.7` version, if we want to create virtual environment with different python version, we can change from script.
  - It will also activate environment for the django project and install all dependencies from `requirements` directory `.txt` file with `local.txt` and `production.txt`.

  ```
    sh setup_environments/03-setup-virtualenv.sh
  ```

**Install pre-commit hooks:**

```sh
pre-commit install
```

## Project Directory/File Structure

```
django-design-pattern-architecture/
        app_modules/
            apis/
                base/
                     renderers.py
                <--other modules directory-->/
                urls.py
        core_apps/
        	base/
        		models.py
        	<--django app modules-->/
        static/
        	vender/
        		css/
        		js/
        	webapp/
        		assets/
        		css/
        		js/
        templates/
        	webapp/
        	<--django app templates>/
        utils/
        web_apps/
        	base/
        		mixins.py
        		views.py
        	<-- django app modules web app directory -->/
        	apps.py
        	urls.py
        	views.py
        django_circle/
        	settings/
        		base.py
        		local.py
        		production.py
        		test.py
        	asgi.py
        	urls.py
        	wsgi.py
        requirements/
        	base.txt
        	local.txt
        	production.txt
        setup_environments/
        	<-- Shell scripts files for environment setup -->
        .env.example
        .gitignore
        .pre-commit-config.yaml
        manage.py
        README.md
```

### Run Server

#### Django Server

```sh
python manage.py runserver
```

# License

© Django Circle - All rights reserved.

### Contact

Django Circle - djangocircle@gmail.com

http://djangocircle.com/
