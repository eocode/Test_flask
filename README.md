<div align="center">
  <img width="64" src="https://avatars1.githubusercontent.com/u/66532658?s=400&u=f2457dec96897c5dbc843372ec8b325589ab84d5&v=4" alt="cookiecutter-django-rest">
  <h3 align="center">App</h3>
  <p align="center">
    Flask best practices template
  </p>
  <p align="center">
    <a href="https://github.com/ActivandoIdeas/Cookiecutter-Django-AppEngine-GitLab/blob/master/LICENSE">
      	<img src="https://img.shields.io/badge/License-BSD3-blue.svg"  alt="license badge"/>
    </a>
    <a href="https://travis-ci.org/ActivandoIdeas/Cookiecutter-Django-AppEngine-GitLab">
        <img src="https://img.shields.io/travis/ActivandoIdeas/Cookiecutter-Django-AppEngine-GitLab.svg?label=django-cookiecutter" alt="Build Status">
    </a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/pypi/pyversions/Django.svg?style=flat-square"  alt="python badge">
    </a>
  </p>
</div>

## Demo

Your demo project

## How to clone

You can clone this repository

    git clone https://github.com/eocode/App
    
## File structure

* **app** (Flask configurations project)
  * **init** (Create and initialize app)
  * **config** (All settings environments)
  * **connection** (Settings for SQLAlchemy)
  * **envs** (Injectable envs in app)
  * **commands** (Tools for switch environments and other quick utilities)
  * **img** (Project images for documentation)
  * **requirements** (Dependencies files for app)
* **test**
* **migrations** (Migrations files, not public, disabled by gitignore)
* **labs** (Labs for create quick scripts for analize problem, you can disabled by gitignore)
* **modules** Your project modules
  * **example** (Main blueprint Flask module)

## Dependencies

* Flask
* python-dotenv
* Flask-sqlalchemy
* Psycopg2
* Pytest
* Flask-migrate

## Environment configuration

Edit envs/.env.* and add your configuration

Then execute:
```sh
python app/commands/environment.py development
```

Available params:
* production
* testing
* development

## Use on local
To install this project just type

Create virtual enviroment:

    $ python -m venv env

Active your enviroment

Install dependencies

    $ pip install -r requirements.txt

Run the project

    $ flask run
    
## Dockerized app

Start app

```bash
docker compose up -d
```

Stop app

```bash
docker compose down
```

Rebuild app

```bash
docker-compose up -d --build
```

Access to command line interface

```bash
docker exec -it flask-app bash
```

## Run migrations

By default migrations foldar has been add to .gitignore

Open Terminal

```bash
docker exec -it flask-app bash
```

Init database migrations

```bash
flask db init
```

Generate migrations

```bash
flask db migrate
```

Run migrations

```bash
flask db upgrade
```

Show more commands

```bash
flask db
```

## Run tests

On Docker

```sh
docker-compose exec queens-app pytest
```

or only

pytest

### Ejecute coverage report

```sh
coverage run -m pytest
coverage report
coverage html
```

## Preview

Your image project previews

## How to contribute

* Review our code of conduct

# License

View in https://github.com/eocode/App/blob/master/LICENSE