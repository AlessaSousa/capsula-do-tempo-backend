# ChronoBox

## Descrição

Backend da aplicação Cápsula do Tempo (ChronoBox) desenvolvido em Python com FastAPI e utilizando Docker para orquestração de containers.  
A aplicação permite cadastro/login de usuários criação e envio programado de cápsulas via email.

---

## Pré-requisitos

#### Docker instalado 
    https://docs.docker.com/get-docker/ 

#### Git instalado (opcional para clonar o repositório)
    https://git-scm.com/downloads

#### Visual Studio Code (ou outra IDE de sua preferência)
    https://code.visualstudio.com/download

#### Python
    https://www.python.org/downloads

---

## Instalação

#### Clone o repositório:  
    git clone https://github.com/AlessaSousa/capsula-do-tempo-backend.git

    cd capsula-do-tempo-backend

#### Criar arquivo .env com as seguintes váriaveis: 
    DATABASE_URL=postgresql://postgres:postgre123@postgres:5432/capsula_tempo_db
    SECRET_KEY=sua-chave-secreta
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=465
    SMTP_USER=user@exemplo.com
    SMTP_PASSWORD=sua-senha

---

## Estrutura de Pastas
```bash
capsula-tempo-backend/
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
```
---

## Funcionalidades
- Cadastro de usuários com validação e hash de senha
- Login com autenticação JWT
- Criação e listagem de cápsulas do tempo
- Envio programado de cápsulas via email 

---

## Execução
#### Subir containers
    docker compose up --build
#### Remover containers
    docker compose down
#### Rodar backend localmente (fora do docker)
    py run.py
#### Acesse a documentação: 
    http://localhost:8000/docs

---

## Licença
MIT License © Alessandra de Sousa