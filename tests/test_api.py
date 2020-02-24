import json
import pytest

from app import create_app, db
from app.models import Todo

ERRORS = {
    400: "Bad Request", 
    401: "Unauthorized",
    403: "Forbidden", 
    404: "Not found",
    500: "Internal Server Error"}


@pytest.fixture(scope='module')
def client():
    flask = create_app("testing")
    client = flask.test_client()

    # Establish an application context before running the tests.
    ctx = flask.app_context()
    ctx.push()
    
    yield client  # this is where the testing happens

    ctx.pop()


@pytest.fixture()
def database(request):
    with db.database:
        db.database.create_tables([Todo])

    yield db.database

    with db.database:
        db.database.rollback()

@pytest.fixture()
def new_todo():
    with db.database:
        Todo.create_table()
        todo = Todo(task="make eggs")
        todo.save()

    return todo

def get_headers():
    return {"Accept": "application/json", "Content-Type": "application/json"}

def error(response, expected_status_code):
    assert response.status_code == expected_status_code
    json_response = json.loads(response.data)
    assert json_response["error"] == ERRORS[expected_status_code]
    
    return True


### TESTS

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_root(client):
    response = client.get("/api/")
    assert response.status_code == 200

def test_get_todos(client):
    response = client.get("/api/todos/")
    assert response.status_code == 200
    assert type(response.json["todos"]) == type([])

def test_post_todo(client, database):
    response = client.post(
        "/api/todos/", headers=get_headers(),
        data=json.dumps({"task": "do laundry"}))

    assert response.status_code == 201
    assert response.json["task"] == "do laundry"

def test_post_todo_bad_request_data(client, database):
    response = client.post(
        "/api/todos/", headers=get_headers(),
        data=json.dumps({"mask": 5}))
    
    assert response.status_code == 400

def test_get_todo(client, database, new_todo):
    i = new_todo.id
    response = client.get(f"/api/todos/{i}")
    
    assert response.status_code == 200
    assert response.json["task"] == "make eggs"

def test_get_todo_not_found(client, database):
    response = client.get("/api/todos/9000")
    
    assert response.status_code == 404

def test_get_todo_invalid_id(client, database):
    response = client.get("/api/todos/eggs")

    assert response.status_code == 404
    assert b"404 Not Found" in response.data

def test_put_todo(client, database, new_todo):
    i = new_todo.id 
    response = client.put(
        f"/api/todos/{i}", headers=get_headers(),
        data=json.dumps({"task": "make omlette"}))

    assert response.status_code == 200
    assert response.json["task"] == "make omlette"

def test_put_todo_not_found(client, database): 
    response = client.put(
        f"/api/todos/9000", headers=get_headers(),
        data=json.dumps({"task": "make omlette"}))
    
    assert response.status_code == 404

def test_put_todo_key_error(client, database, new_todo):
    i = new_todo.id
    response = client.put(
        f"/api/todos/{i}", headers=get_headers(),
        data=json.dumps({"bad_key": 5}))
    
    assert response.status_code == 400

def test_delete_todo(client, database, new_todo):
    i = new_todo.id
    response = client.delete(f"/api/todos/{i}")
    assert response.status_code == 204

def test_delete_todo_not_found(client, database):
    response = client.delete("/api/todos/9000")
    assert response.status_code == 404

def  test_delete_todo_invalid_id(client, database, new_todo):

   response = client.delete("/api/todos/eggs")
   assert response.status_code == 404
   assert b"404 Not Found" in response.data