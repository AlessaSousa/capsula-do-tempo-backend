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
capsula-do-tempo-backend/
├── app/                    
│   ├── core/   
|       ├── config.py
|       ├── depedencies.py    
|   ├── crud/
|       ├──capsule.py        
│   ├── models/  
|       ├── capsule.py
|       ├── user.py           
│   ├── routes/   
|       ├── auth.py
|       ├──capsule.py           
│   ├── schemas/
|       ├── capsule.py
|       ├── user.py
|   ├── service/ 
|       ├── email.py
|       ├── scheduler.py             
│   ├── utils/ 
|       ├── auth.py
|   ├── database.py           
│   └── main.py             
│
├── dockerfile               
├── docker-compose.yml       
├── requirements.txt         
├── .env  
├── venv
├── .gitignore                   
├── README.md   
├── run.py            

## Funcionalidades
### Cadastro de usuários com validação e hash de senha
### Login com autenticação JWT
### Criação e listagem de cápsulas do tempo
### Envio programado de cápsulas via email 


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

## Licença
MIT License © Alessandra de Sousa