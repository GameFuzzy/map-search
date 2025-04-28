# map-search
[![codecov](https://codecov.io/gh/GameFuzzy/map-search/graph/badge.svg?token=KjptTS4I7H)](https://codecov.io/gh/GameFuzzy/map-search)
[![Tests](https://github.com/GameFuzzy/map-search/actions/workflows/test.yml/badge.svg)](https://github.com/GameFuzzy/map-search/actions/workflows/test.yml)
[![Publish Docker image](https://github.com/GameFuzzy/map-search/actions/workflows/docker-image.yml/badge.svg)](https://github.com/GameFuzzy/map-search/actions/workflows/docker-image.yml)

## Dependencies

`docker`, `docker-compose`

## Initial setup

### Setting up the Docker Compose environment

```
$ cd /path/to/project
```
```
$ cp -r sample/env .env
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

Navigate to http://localhost:8000/api/docs to experiment with the API

## Testing

```
$ docker compose run --rm --build web python manage.py test
```

## Verify GameFuzzy/map-search image build provenance

```
$ gh attestation verify oci://index.docker.io/gamefuzzy/map-search -R GameFuzzy/map-search
```
