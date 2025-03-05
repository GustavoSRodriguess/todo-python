"""API endpoints para tarefas."""
from flask import Blueprint, request, jsonify
from app import db
from app.models.todo import Todo
from datetime import datetime
from marshmallow import Schema, fields, validate, ValidationError

todo_blueprint = Blueprint('todo', __name__)

# Schema para validação
class TodoSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(allow_none=True)
    completed = fields.Bool(default=False)
    priority = fields.Int(validate=validate.Range(min=1, max=3), default=1)
    due_date = fields.DateTime(allow_none=True)

todo_schema = TodoSchema()

@todo_blueprint.route('/todos', methods=['GET'])
def get_todos():
    """Listar todas as tarefas."""
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos]), 200

@todo_blueprint.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Obter uma tarefa específica."""
    todo = Todo.query.get_or_404(todo_id)
    return jsonify(todo.to_dict()), 200

@todo_blueprint.route('/todos', methods=['POST'])
def create_todo():
    """Criar uma nova tarefa."""
    data = request.get_json()
    
    # Validar dados
    try:
        validated_data = todo_schema.load(data)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    
    # Criar tarefa
    todo = Todo(
        title=validated_data['title'],
        description=validated_data.get('description'),
        completed=validated_data.get('completed', False),
        priority=validated_data.get('priority', 1),
        due_date=validated_data.get('due_date')
    )
    
    db.session.add(todo)
    db.session.commit()
    
    return jsonify(todo.to_dict()), 201

@todo_blueprint.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Atualizar uma tarefa existente."""
    todo = Todo.query.get_or_404(todo_id)
    data = request.get_json()
    
    # Validar dados
    try:
        validated_data = todo_schema.load(data)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    
    # Atualizar campos
    todo.title = validated_data.get('title', todo.title)
    if 'description' in validated_data:
        todo.description = validated_data['description']
    if 'completed' in validated_data:
        todo.completed = validated_data['completed']
    if 'priority' in validated_data:
        todo.priority = validated_data['priority']
    if 'due_date' in validated_data:
        todo.due_date = validated_data['due_date']
    
    db.session.commit()
    
    return jsonify(todo.to_dict()), 200

@todo_blueprint.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Excluir uma tarefa."""
    todo = Todo.query.get_or_404(todo_id)
    
    db.session.delete(todo)
    db.session.commit()
    
    return jsonify({"message": "Tarefa excluída com sucesso"}), 200

@todo_blueprint.route('/todos/<int:todo_id>/toggle', methods=['PATCH'])
def toggle_todo(todo_id):
    """Alternar o status de conclusão da tarefa."""
    todo = Todo.query.get_or_404(todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    
    return jsonify(todo.to_dict()), 200