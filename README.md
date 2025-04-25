# map-search

## Dependencies

`docker`, `docker-compose`

## Initial setup

### Setting up the Docker stack

```
$ cd /path/to/project
```
```
$ cp sample/env .env
```
Change the credentials in `.env/db.env` and `.env/django.env` to something
   secure
```
$ docker compose up -d
```
> **_NOTE:_**  Add `--build` if you want to build the image from
   source

### Setting up the database

Either:

```
$ docker compose exec web python manage.py migrate
```

to start off with an empty user database

or

```
$ cat sample/db.sql | docker compose exec -T user-db psql -U postgres -d postgres
```

to restore the included sample database

> **_NOTE:_**  If you have changed `DATABASE_DB` and/or `DATABASE_USER` in `.env/db.env` then the above command will have to be modified to reflect that


## Usage

While the docker stack is running http://localhost:8000/api/docs can be used to experiment with the API

## Verify GameFuzzy/map-search build provenance

```
$ gh attestation verify oci://index.docker.io/gamefuzzy/map-search -R GameFuzzy/map-search
```
