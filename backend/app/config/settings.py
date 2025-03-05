"""Configurações da aplicação."""
import os
from environs import Env
from datetime import timedelta

env = Env()
env.read_env()

# Caminhos do projeto
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Configurações básicas
ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SECRET_KEY = env.str("SECRET_KEY", default="super-secret-key")

# Configurações do banco de dados
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL", default="sqlite:///todo_app.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configurações JWT
JWT_SECRET_KEY = env.str("JWT_SECRET_KEY", default="jwt-super-secret")
JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=env.int("JWT_ACCESS_TOKEN_EXPIRES", default=86400))