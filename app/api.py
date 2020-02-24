# -*- coding: utf-8 -*-
from flask import abort, jsonify, make_response, request, url_for, Blueprint
from playhouse.shortcuts import dict_to_model, model_to_dict 
from .models import Todo


api = Blueprint("api", __name__)


@api.route("/")
def get_root():
    return jsonify({}), 200


@api.route("/todos/")
def get_todos():
    return jsonify({
        "todos": list(model_to_dict(todo)
        for todo in Todo.select())}), 200


@api.route("/todos/", methods=["POST"])
def add_todo():
    try:
        todo = Todo(task=request.json.get("task"))
        todo.save()
    except:
        abort(400)
    return jsonify(model_to_dict(todo)), 201


@api.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    try:
        todo = Todo.get(Todo.id == todo_id)
    except Todo.DoesNotExist:
        abort(404)
    except:
        abort(400)
    return jsonify(model_to_dict(todo)), 200

@api.route("/todos/<int:todo_id>", methods=["PUT"])
def put_todo(todo_id):
    try:
        todo = Todo.get(Todo.id == todo_id)
        todo.task = request.json.get("task")
        todo.save()
    except Todo.DoesNotExist:
        abort(404)
    except:
        abort(400)
    return jsonify(model_to_dict(todo)), 200

@api.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    try:
        todo = Todo.get(Todo.id == todo_id)
        if not todo.delete_instance():
            abort(404)
    except Todo.DoesNotExist:
        abort(404)
    except:
        abort(400)
    return jsonify({}), 204


@api.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad Request"}), 400)


@api.errorhandler(401)
def unauthorized(error):
    return make_response(jsonify({"error": "Unauthorized"}), 401)


@api.errorhandler(403)
def forbidden(error):
    return make_response(jsonify({"error": "Forbidden"}), 403)


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)

