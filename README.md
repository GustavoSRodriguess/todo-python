# Todo App com Vue.js, Flask e Docker

Um aplicativo de gerenciamento de tarefas desenvolvido com Vue.js 3 no frontend, Flask no backend, estilizado com Tailwind CSS e conteinerizado com Docker.

## Tecnologias Utilizadas

### Frontend
- Vue.js 3 (Composition API)
- Tailwind CSS
- Vue Router
- Axios

### Backend
- Python Flask
- Flask-RESTful
- SQLAlchemy ORM
- PostgreSQL
- JWT Authentication

### DevOps
- Docker
- Docker Compose

## Pré-requisitos

- Docker
- Docker Compose

## Como Executar

1. Clone o repositório:
   ```bash
   git clone <url-do-repositório>
   cd todo-app
   ```

2. Inicie os containers com Docker Compose:
   ```bash
   docker-compose up -d
   ```

3. Inicialize o banco de dados:
   ```bash
   docker-compose exec backend flask db init
   docker-compose exec backend flask db migrate -m "Initial migration"
   docker-compose exec backend flask db upgrade
   ```

4. Acesse a aplicação:
   - Frontend: http://localhost:8080
   - Backend API: http://localhost:5000/api/v1
   - PgAdmin (gerenciamento do banco de dados): http://localhost:5050
     - Email: admin@admin.com
     - Password: admin

## Endpoints da API

- `GET /api/v1/todos`: Listar todas as tarefas
- `GET /api/v1/todos/<id>`: Obter uma tarefa específica
- `POST /api/v1/todos`: Criar uma nova tarefa
- `PUT /api/v1/todos/<id>`: Atualizar uma tarefa existente
- `DELETE /api/v1/todos/<id>`: Excluir uma tarefa
- `PATCH /api/v1/todos/<id>/toggle`: Alternar o status de conclusão da tarefa

## Estrutura do Projeto

```
todo-app/
├── backend/              # Código do servidor Flask
│   ├── app/              # Pacote principal da aplicação
│   │   ├── __init__.py   # Inicialização da aplicação
│   │   ├── api/          # Endpoints da API
│   │   ├── models/       # Modelos de dados (SQLAlchemy)
│   │   └── config/       # Configurações
│   ├── tests/            # Testes unitários
│   ├── Dockerfile        # Configuração Docker para o backend
│   └── requirements.txt  # Dependências Python
├── frontend/             # Código do cliente Vue.js
│   ├── src/              # Código-fonte Vue
│   │   ├── components/   # Componentes Vue
│   │   ├── views/        # Páginas da aplicação
│   │   ├── router/       # Configuração de rotas
│   │   ├── store/        # Gerenciamento de estado (Vuex)
│   │   ├── App.vue       # Componente raiz
│   │   └── main.js       # Ponto de entrada
│   ├── public/           # Arquivos estáticos
│   └── Dockerfile        # Configuração Docker para o frontend
├── docker-compose.yml    # Orquestração dos serviços
└── README.md             # Documentação
```

## Desenvolvimento

Para desenvolvimento local sem Docker:

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
flask run
```

### Frontend
```bash
cd frontend
npm install
npm run serve
```

## Melhorias Futuras

- Implementar autenticação de usuários
- Adicionar categorias e etiquetas para tarefas
- Criar recurso de subtarefas
- Adicionar notificações e lembretes
- Implementar sincronização offline com IndexedDB