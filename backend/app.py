from app import create_app

app = create_app()

# Permitir CORS para o frontend
CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)