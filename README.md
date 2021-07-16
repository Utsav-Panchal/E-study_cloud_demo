# Maintainable E-Study Django Design Pattern Architecture



### Table of Content:
- [Overview](#overview)
- [What is Django Circle?](#what-is-E-Study?)
- [Benefits to use this repository for django project](#benefits-to-use-this-repository-for-django-project)
- [Features of E-Study Django Design pattern architecture](#features-of-django-design-pattern-architecture)
- [Installation](#instalation)
- [Requirements](#requirements)
- [Project Directory/File Structure](#project-directory/file-structure)


# Overview
- This is a simple, easy to understand and maintainable django project architecture which contains base architecture for any project.
- To start new django project, don't need to take care and research to setup basic process and installation process. All things will get here.


# What is Django Circle ?
- Django Circle is a community to share solutions of problem which can be solved by using django framework.

# Benefits to use this repository for django project
- No need to worry about setup process. Now it is simple process, just need to clone and ready to start work on it.
- Scalable application base structure
- Easy to maintain and modify
- Ready architecture to work with different environments : `local`, `staging`, `production`.


# Features of Django Design Pattern Architecture

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
git clone https://github.com/Utsav-Panchal/E-study_cloud_demo.git
```

**Install pre-commit hooks:**

```sh
pre-commit install
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

## Project Directory/File Structure

```
django-design-pattern-architecture
├── app_modules
│   ├── apis
│   │   ├── auth
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── base
│   │   │   ├── renderers.py
│   │   │   └── renderers.py
│   │   └── urls.py
│   ├── core_apps
│   │   ├── base
│   │   │   ├── models.py
│   │   └── users
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── models.py
│   │       └── signals.py
│   ├── static
│   │   ├── vender
│   │   │   ├── charts
│   │   │   ├── css
│   │   │   └── js
│   │   └── webapp
│   │       ├── assets
│   │       │   └── img
│   │       ├── css
│   │       │   └── styles.css
│   │       └── js
│   │           └── scripts.js
│   ├── templates
│   │   ├── account
│   │   │   ├── email_confirm.html
│   │   │   ├── login.html
│   │   │   ├── password_reset_done.html
│   │   │   ├── password_reset_from_key_done.html
│   │   │   ├── password_reset_from_key.html
│   │   │   ├── password_reset.html
│   │   │   ├── signup.html
│   │   │   └── verification_sent.html
│   │   └── webapp
│   │       ├── base.html
│   │       ├── includes
│   │       │   ├── header.html
│   │       │   └── sidebar.html
│   │       ├── index.html
│   │       ├── partials
│   │       │   ├── form_hidden_fields.html
│   │       │   └── messages.html
│   │       └── users
│   │           └── profile.html
│   ├── utils
│   └── web_apps
│       ├── apps.py
│       ├── authentication
│       ├── base
│       │   ├── mixins.py
│       │   └── views.py
│       ├── urls.py
│       ├── users
│       │   ├── forms.py
│       │   ├── urls.py
│       │   └── views.py
│       └── views.py
├── django_circle
│   ├── asgi.py
│   ├── settings
│   │   ├── base.py
│   │   ├── local.py
│   │   ├── production.py
│   │   └── test.py
│   ├── urls.py
│   └── wsgi.py
├── .env
├── .env.example
├── .gitignore
├── manage.py
├── .pre-commit-config.yaml
├── README.md
├── requirements
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
└── setup_environments
    ├── 01-install-python3x.sh
    ├── 02-install-postgresql.sh
    └── 03-setup-virtualenv.sh
```

### Run Server

#### Django Server

```sh
python manage.py runserver
```

# License

© E-Study - All rights reserved.

### Contact

E-Study - putsavnarendra1998@gmail.com


