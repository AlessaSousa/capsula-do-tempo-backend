# ChronoBox

## Descrição

Backend da aplicação Cápsula do Tempo (ChronoBox) desenvolvido em FastAPI com banco PostgreSQL utilizando Docker Compose para orquestração dos containers.  
Permite cadastro/login de usuários criação e envio programado de cápsulas via email.

---

## Tecnologias

- Python 3.12  
- FastAPI  
- PostgreSQL 15  
- SQLAlchemy  
- Pydantic  
- Docker 
- Uvicorn  
- python-dotenv  
- passlib (hash de senhas)  
- python-jose (JWT)  
- email-validator  

---

## Pré-requisitos

- Docker instalado https://docs.docker.com/get-docker/ 
- Git instalado (opcional para clonar o repositório)

---

## Instalação

1. Clone o repositório:  
    git clone https://github.com/AlessaSousa/capsula-do-tempo-backend.git
    cd capsula-do-tempo-backend

---

## Estrutura de Pastas
ccapsula-tempo-backend/
├── app/
│   ├── core/                 # Configurações globais e dependências
│   │   ├── config.py
│   │   └── depedencies.py
│   ├── crud/                 # Operações com o banco de dados
│   │   └── capsule.py
│   ├── models/               # Modelos SQLAlchemy
│   │   ├── capsule.py
│   │   └── user.py
│   ├── routes/               # Rotas da API
│   │   ├── auth.py
│   │   └── capsule.py
│   ├── schemas/              # Schemas Pydantic (validação de dados)
│   │   ├── capsule.py
│   │   └── user.py
│   ├── service/              # Lógica de envio de e-mail e agendamento
│   │   ├── email.py
│   │   └── scheduler.py
│   ├── utils/                # Utilitários auxiliares
│   │   └── auth.py
│   ├── database.py           # Conexão com o banco de dados
│   └── main.py               # Ponto de entrada da aplicação
│
├── dockerfile                # Dockerfile da aplicação FastAPI
├── docker-compose.yml        # Orquestração dos serviços com Docker
├── requirements.txt          # Dependências da aplicação
├── .env                      # Variáveis de ambiente
├── .gitignore                # Arquivos a serem ignorados pelo Git
├── venv/                     # Ambiente virtual (ignorado no container)
├── run.py                    # Execução auxiliar (opcional)
└── README.md                 # Este arquivo

## Funcionalidades
### Cadastro de usuários com validação e hash de senha
### Login com autenticação JWT
### Criação e listagem de cápsulas do tempo
### Envio programado de cápsulas via email 

---

## Execução
### Subir containers
    docker compose up --build

    Isso irá:
    - Baixar as imagens necessárias
    - Construir a imagem do backend
    - Subir container PostgreSQL e FastAPI

    Acesse a documentação: 
    - http://localhost:8000/docs
### Remover containers
    docker compose down
### Rodar backend localmente (fora do docker)
    py run.py

---

## Licença
MIT License © Alessandra de Sousa