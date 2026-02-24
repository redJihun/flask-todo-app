# /api/todos 엔드포인트
from flask import Blueprint, jsonify, request
from ..models.todo import Todo
from ..services.todo_service import get_todos, create_todo

api_bp = Blueprint('api', __name__)

@api_bp.route('/todos', methods=['GET'])
def list_todos():
    return jsonify(get_todos())

@api_bp.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    todo = create_todo(data['content'])
    return jsonify(todo), 201
