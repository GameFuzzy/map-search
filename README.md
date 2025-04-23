# map-search

## Dependencies

`docker`, `docker-compose`

## Initial setup

### Setting up the docker stack

1. `cd /path/to/project`
2. `cp sample/env env`
3. Change the credentials in `env/db.env` and `env/django.env` to something
   secure
4. `docker compose up -d` (add `--build` if you want to build the image from
   source)

### Setting up the database

Either:

`docker compose exec user-db python manage.py migrate`

to start off with an empty user database

or

`cat sample/db.sql | docker compose exec -T user-db psql -U postgres -d postgres`

to restore a sample database

> **_NOTE:_**  If you have changed `DATABASE_DB` and/or `DATABASE_USER` in `env/db.env` then the above command will have to be modified to reflect that


## Usage

While the docker stack is running http://localhost:8000/api/docs can be used to experiment with the API
