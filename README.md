# Authentication with Flask, React, and Docker

[![pipeline status](https://gitlab.com/sbathgate/flask-tdd-docker/badges/master/pipeline.svg)](https://gitlab.com/sbathgate/flask-tdd-docker/commits/master)

## Quick start
* Clone GitLab Repo: `$ git clone https://gitlab.com/sbathgate/flask-tdd-docker.git`
* Switch to project root: `$ cd flask-tdd-docker/`
* Build the images: `$ docker-compose build`
* Run the containers: `$ docker-compose up -d`
* Create the database: `$ docker-compose exec users python manage.py recreate_db`
* Seed the database: `$ docker-compose exec users python manage.py seed_db`


## File Structure
#### Within the download you'll find the following directories and files:
```
├── .coverage
├── .coveragerc
├── .dockerignore
├── .gitignore
├── .gitlab-ci.yml
├── Dockerfile
├── Dockerfile.prod
├── README.md
├── docker-compose.yml
├── entrypoint.sh
├── htmlcov
├── manage.py
├── project
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── ping.py
│   │   └── users
│   │       ├── __init__.py
│   │       ├── admin.py
│   │       ├── models.py
│   │       ├── crud.py
│   │       └── views.py
│   ├── config.py
│   ├── db
│   │   ├── Dockerfile
│   │   └── create.sql
│   └── tests
│       ├── __init__.py
│       ├── conftest.py
│       ├── pytest.ini
│       ├── test_admin.py
│       ├── test_config.py
│       ├── test_ping.py
│       ├── test_users.py
│       └── test_users_unit.py
├── release.sh
├── requirements-dev.txt
├── requirements.txt
└── setup.cfg
```

## Common Commands
#### Build the images:
```$ docker-compose build```

#### Run the containers:
```$ docker-compose up -d```

#### Create the database:
```$ docker-compose exec users python manage.py recreate_db```

#### Seed the database:
```$ docker-compose exec users python manage.py seed_db```

#### Run the tests:
```$ docker-compose exec users python -m pytest "project/tests" -p no:warnings```

#### Run the tests with coverage:
```$ docker-compose exec users python -m pytest "project/tests" -p no:warnings --cov="project"```

#### Lint:
```$ docker-compose exec users flake8 project```

#### Run Black and isort with check options:
```$ docker-compose exec users black project --check```
```$ docker-compose exec users /bin/sh -c "isort project/**/*.py --check-only"```

#### Make code changes with Black and isort:
```$ docker-compose exec users black project```
```$ docker-compose exec users /bin/sh -c "isort project/**/*.py"```

### Other Commands
#### To stop the containers:
```$ docker-compose stop```

#### To bring down the containers:
```$ docker-compose down```

#### Want to force a build?
```$ docker-compose build --no-cache```

#### Remove images:
```$ docker rmi $(docker images -q)```

### Postgres
#### Want to access the database via psql?
```$ docker-compose exec users-db psql -U postgres```

##### Then, you can connect to the database and run SQL queries. For example:
```# \c users_dev```
```# select * from users;```