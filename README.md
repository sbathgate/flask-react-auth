# Authentication with Flask, React, and Docker

[![pipeline status](https://gitlab.com/sbathgate/flask-react-auth/badges/master/pipeline.svg)](https://gitlab.com/sbathgate/flask-tdd-docker/commits/master)

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
├── .gitignore
├── .gitlab-ci.yml
├── README.md
├── docker-compose.yml
├── release.sh
└── services
    ├── client
    │   ├── .dockerignore
    │   ├── .gitignore
    │   ├── Dockerfile
    │   ├── README.md
    │   ├── coverage
    │   ├── package-lock.json
    │   ├── package.json
    │   ├── public
    │   │   ├── favicon.ico
    │   │   ├── index.html
    │   │   ├── logo192.png
    │   │   ├── logo512.png
    │   │   ├── manifest.json
    │   │   └── robots.txt
    │   └── src
    │       ├── components
    │       │   ├── AddUser.jsx
    │       │   ├── UsersList.jsx
    │       │   └── __tests__
    │       │       ├── AddUser.test.jsx
    │       │       ├── UsersList.test.jsx
    │       │       └── __snapshots__
    │       │           ├── AddUser.test.jsx.snap
    │       │           └── UsersList.test.jsx.snap
    │       ├── index.js
    │       └── setupTests.js
    └── users
        ├── .coverage
        ├── .coveragerc
        ├── .dockerignore
        ├── Dockerfile
        ├── Dockerfile.prod
        ├── entrypoint.sh
        ├── manage.py
        ├── project
        │   ├── __init__.py
        │   ├── api
        │   │   ├── __init__.py
        │   │   ├── ping.py
        │   │   └── users
        │   │       ├── __init__.py
        │   │       ├── admin.py
        │   │       ├── crud.py
        │   │       ├── models.py
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
        ├── requirements-dev.txt
        ├── requirements.txt
        └── setup.cfg
```

## Common Commands
### Docker Compose
#### Set the `REACT_APP_USERS_SERVICE_URL` environment variable:
```$ export REACT_APP_USERS_SERVICE_URL=http://localhost:5001```

#### Build the images:
```$ docker-compose build```

#### Build and spin up the new containers:
```$ docker-compose up -d --build```

#### To stop the containers:
```$ docker-compose stop```

#### To bring down the containers:
```$ docker-compose down```

### Client
#### Run the tests without coverage:
```$ docker-compose exec client npm test```

#### Run the tests with coverage:
```$ docker-compose exec client npm test --coverage```

#### Check formatting with Prettier:
```$ docker-compose exec client npm run prettier:check```

#### Lint with eslint:
```$ docker-compose exec client npm run lint```

### Server
#### Create the database:
```$ docker-compose exec users python manage.py recreate_db```

#### Seed the database:
```$ docker-compose exec users python manage.py seed_db```

#### Run the tests without coverage:
```$ docker-compose exec users python -m pytest "project/tests" -p no:warnings```

#### Run the tests with coverage:
```$ docker-compose exec users python -m pytest "project/tests" -p no:warnings --cov="project"```

#### Lint with Flake8:
```$ docker-compose exec users flake8 project```

#### Run Black and isort with check options:
```$ docker-compose exec users black project --check```

```$ docker-compose exec users /bin/sh -c "isort project/**/*.py --check-only"```

#### Make code changes with Black and isort:
```$ docker-compose exec users black project```

```$ docker-compose exec users /bin/sh -c "isort project/**/*.py"```

### Postgres
#### Want to access the database via psql?
```$ docker-compose exec users-db psql -U postgres```

##### Then, you can connect to the database and run SQL queries. For example:
```# \c users_dev```
```# select * from users;```

### Other Commands
#### Want to force a build?
```$ docker-compose build --no-cache```

#### Remove images:
```$ docker rmi $(docker images -q)```