# Tiny Flask

A template SPA built with Vuejs and Flask.

Backend: Flask, Peewee, Sqlite, and Pytest
Frontend: Vuejs and Axios

## Install

### Production

`$ pip install -r requirements.txt`

### Development

`$ pip install -e .`
`$ FLASK_APP=run.py`
`$ FLASK_ENV=development`
`$ flask initdb`
`$ flask run`

## Testing

`$ pytest`

## TODO

- add validation to peewee model(s)