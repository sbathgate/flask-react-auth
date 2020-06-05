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
├── Dockerfile.deploy
├── README.md
├── docker-compose.yml
├── makefile
├── release.sh
└── services
    ├── client
    │   ├── .dockerignore
    │   ├── .eslintrc.json
    │   ├── .gitignore
    │   ├── Dockerfile
    │   ├── Dockerfile.ci
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
    │       ├── App.jsx
    │       ├── components
    │       │   ├── About.jsx
    │       │   ├── AddUser.jsx
    │       │   ├── LoginForm.jsx
    │       │   ├── Message.jsx
    │       │   ├── NavBar.css
    │       │   ├── NavBar.jsx
    │       │   ├── RegisterForm.jsx
    │       │   ├── UserStatus.jsx
    │       │   ├── UsersList.jsx
    │       │   ├── __tests__
    │       │   │   ├── About.test.jsx
    │       │   │   ├── AddUser.test.jsx
    │       │   │   ├── App.test.jsx
    │       │   │   ├── LoginForm.test.jsx
    │       │   │   ├── Message.test.jsx
    │       │   │   ├── NavBar.test.jsx
    │       │   │   ├── RegisterForm.test.jsx
    │       │   │   ├── UserStatus.test.jsx
    │       │   │   ├── UsersList.test.jsx
    │       │   │   └── __snapshots__
    │       │   │       ├── About.test.jsx.snap
    │       │   │       ├── AddUser.test.jsx.snap
    │       │   │       ├── App.test.jsx.snap
    │       │   │       ├── LoginForm.test.jsx.snap
    │       │   │       ├── Message.test.jsx.snap
    │       │   │       ├── NavBar.test.jsx.snap
    │       │   │       ├── RegisterForm.test.jsx.snap
    │       │   │       ├── UserStatus.test.jsx.snap
    │       │   │       └── UsersList.test.jsx.snap
    │       │   └── form.css
    │       ├── index.js
    │       └── setupTests.js
    ├── nginx
    │   └── default.conf
    └── users
        ├── .coverage
        ├── .coveragerc
        ├── .dockerignore
        ├── Dockerfile
        ├── Dockerfile.prod
        ├── entrypoint.sh
        ├── htmlcov
        ├── manage.py
        ├── project
        │   ├── __init__.py
        │   ├── api
        │   │   ├── __init__.py
        │   │   ├── auth.py
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
        │       ├── test_auth.py
        │       ├── test_config.py
        │       ├── test_ping.py
        │       ├── test_user_model.py
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

## TODO:
#### My notes:
- [ ] Configure singular setup.cfg for flake8, black and isort.

#### Test-Driven Development with Python, Flask and Docker
- [ ] Database migrations: Manage changes to the database through SQLAlchemy database migrations with the Flask-Migrate extension.

#### Authentication with Flask, React, and Docker
##### Part 3: React Auth - Part 2
- [ ] Write test to ensure UserStatus redirects to login if invalid token.
- [ ] EXPLORE: For added protection, instead of storing refresh tokens in LocalStorage, how would you return tokens from the server in HttpOnly cookies? The Flask-JWT-Extended extension may be worth looking at.
##### Part 3: React Alert Messages
- [ ] Add test to ensure message disappears when 1: a user click the 'x', 2: a new message is flashed, 3: three seconds pass
##### Part 3: Update Components
- [ ] Prevent currently logged in person from deleting themselves.
##### Part 3: Next Steps
- [ ] Test coverage: Add more tests to increase the overall test coverage, making sure to cover any remaining edge cases.
- [ ] Unit tests: Add unit tests (via monkeypatch) to cover the auth routes.
- [ ] DRY out the code: There's plenty of places in the code base that could be refactored.
- [ ] Flask CORS: Instead of allowing requests from any domain, lock down the Flask service by only allowing requests that originate from the Heroku domain.
- [ ] Caching: Add caching (where appropriate) with Flask-Cache.
- [ ] Duplicate usernames: Prevent duplicate usernames in the database.
- [ ] Invalidate refresh tokens: Users can have a number of active refresh tokens. It may be worth controlling this to prevent abuse by only allowing a user to have a single refresh token at time. Create a database table for this and update the client and server-side logic.
- [ ] Blacklist tokens: You may want to create a database table for used access and refresh tokens to prevent abuse. Again, update the client and server-side as necessary.
- [ ] Role based authorization: Add role based authorization. Refer to the "Auth" section in Awesome Flask for more info.
- [ ] Cross tab logout: Incorporate cross browser tab logout by adding an event listener on the refresh token in LocalStorage.
- [ ] Transactional emailing: Add the ability to send transactional emails for email confirmation and password changes.
- [ ] Client side: Add the ability to update a user using the same modal configured for adding a user and prevent the currently logged in user from deleting themselves in the table.
- [ ] Hooks: Refactor the class-based React components to functions with React Hooks. Refer to Primer on React Hooks for more info on Hooks.


## Valuable Notes
If you get a compilation error due to Module not found: Can't resolve 'temp'; try installing temp in the running container:
```$ docker-compose exec client npm install react-router-dom```