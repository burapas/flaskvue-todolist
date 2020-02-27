# Flaskvue-Todolist

A template SPA built with Vuejs and Flask.

Backend: Flask, Peewee, Sqlite (Pytest)

Frontend: Vuejs, Axios


### Production

```
pip install -r requirements.txt
FLASK_APP=run.py
FLASK_ENV=production
flask initdb
flask run
```

### Development

```
pip install -e .
FLASK_APP=run.py
FLASK_ENV=development
flask initdb
flask run
```

## Testing

```
FLASK_APP=run.py
FLASK_ENV=production
pytest
```

## TODO

- add validation to peewee model(s)
