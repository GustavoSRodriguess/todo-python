"""Modelos de dados para tarefas."""
from datetime import datetime
from app import db

class Todo(db.Model):
    """Modelo para tarefas."""
    
    __tablename__ = 'todos'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.Integer, default=1)  # 1: baixa, 2: média, 3: alta
    due_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, title, description=None, completed=False, priority=1, due_date=None):
        self.title = title
        self.description = description
        self.completed = completed
        self.priority = priority
        self.due_date = due_date
    
    def __repr__(self):
        return f"<Todo {self.id}: {self.title}>"
    
    def to_dict(self):
        """Convert to dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'priority': self.priority,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }