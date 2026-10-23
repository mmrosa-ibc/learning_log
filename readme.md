projects/spyke-django/             <-- Raiz do seu Projeto no seu computador
├── Dockerfile                     <-- Receita para o Docker criar a imagem Python
├── docker-compose.yml             <-- Orquestrador dos contêineres e portas (ex: 8080:8000)
├── requirements.txt               <-- Lista de compras do Python (ex: django>=5.0)
├── db.sqlite3                     <-- O arquivo do banco de dados padrão (SQLite)
│
├── manage.py                      <-- O painel de controle do projeto (Gerencia os comandos)
│
├── spykedjango/                   <-- PASTA CONFIGURAÇÃO GLOBAL (Coração do Sistema)
│   ├── __init__.py                <-- Arquivo vazio que diz: "Isso aqui é um pacote Python"
│   ├── settings.py                <-- O arquivo mais importante: TODAS as configurações ficam aqui
│   ├── urls.py                    <-- O roteador principal: decide qual página abrir para cada link
│   ├── asgi.py                    <-- Conexão para servidores assíncronos modernos (WebSockets)
│   └── wsgi.py                    <-- Conexão para servidores web tradicionais (Nginx/Apache)
│
└── menu/                          <-- PASTA DO APP (Módulo específico criado por você)
    ├── __init__.py
    ├── admin.py                   <-- Onde você registra suas tabelas no painel administrativo
    ├── apps.py                    <-- Configurações internas deste módulo específico
    ├── models.py                  <-- Onde você desenha o formato das tabelas do banco de dados
    ├── tests.py                   <-- Onde você escreve testes automatizados para o seu código
    ├── views.py                   <-- A lógica do negócio: processa requisições e envia respostas
    ├── migrations/                <-- Pasta automática: guarda o histórico de mudanças do banco
    │   └── __init__.py
    └── templates/                 <-- Pasta para os seus arquivos HTML
        └── menu/                  <-- SUBPASTA COM O NOME DO APP (A boa prática que evita conflitos)
            └── index.html         <-- O seu arquivo HTML limpo


# criar banco inicial

python manage.py migrate

# rodar os servidor 

python .\manage.py runserver

-------

### criando projeto pelo docker e docker compose

# É necessário colocar os arquivos docker-compose.yml e Dockerfile

# Cria arquivos de configuração django
docker compose run --rm web django-admin startproject nomedoprojeto .

# Subir o container
docker compose up (python manage.py runserver)

# Executar as migrations iniciais (python manage.py migrate)
docker compose exec web python manage.py migrate 

# Criar app
docker compose exec web python manage.py startapp learning_logs

# Criar modelo de migration
docker compose exec web python manage.py makemigrations learning_logs

# Criar migration do modelo criado
docker compose exec web python manage.py migrate

# Criar login e senha para painel de administrador
docker compose exec web python manage.py createsuperuser

# Abrir shell do Django
docker compose exec web python manage.py shell