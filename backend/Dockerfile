FROM python:3.11-slim

WORKDIR /app

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app/__init__.py \
    FLASK_ENV=development

# Instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Exposição da porta
EXPOSE 5000

# Comando para iniciar a aplicação em modo desenvolvimento
CMD ["flask", "run", "--host=0.0.0.0"]