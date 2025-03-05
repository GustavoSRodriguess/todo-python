from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Instâncias dos plugins
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_object="app.config.settings"):
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Configuração da aplicação
    app.config.from_object(config_object)
    
    # Inicializar plugins
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Permitir CORS para o frontend
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Registrar blueprints (rotas API)
    from app.api.todo import todo_blueprint
    app.register_blueprint(todo_blueprint, url_prefix='/api/v1')
    
    # Shell context para usar o Flask shell
    @app.shell_context_processor
    def shell_context():
        return {"app": app, "db": db}
    
    return app