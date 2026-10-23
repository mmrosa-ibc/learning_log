# Learning Log - Spike Django

Este repositório é um spike para aprender e praticar os conceitos básicos do framework Django, utilizando Docker e Docker Compose para o ambiente de desenvolvimento.

## Estrutura do Projeto

```text
projects/learning_log/             <-- Raiz do seu Projeto no seu computador
├── Dockerfile                     <-- Receita para o Docker criar a imagem Python
├── docker-compose.yml             <-- Orquestrador dos contêineres e portas (ex: 8080:8000)
├── requirements.txt               <-- Lista de compras do Python (ex: django>=5.0)
├── db.sqlite3                     <-- O arquivo do banco de dados padrão (SQLite)
│
├── manage.py                      <-- O painel de controle do projeto (Gerencia os comandos)
│
├── learninglog/                   <-- PASTA CONFIGURAÇÃO GLOBAL (Coração do Sistema)
│   ├── __init__.py                <-- Arquivo vazio que diz: "Isso aqui é um pacote Python"
│   ├── settings.py                <-- O arquivo mais importante: TODAS as configurações ficam aqui
│   ├── urls.py                    <-- O roteador principal: decide qual página abrir para cada link
│   ├── asgi.py                    <-- Conexão para servidores assíncronos modernos (WebSockets)
│   └── wsgi.py                    <-- Conexão para servidores web tradicionais (Nginx/Apache)
│
└── learning_logs/                 <-- PASTA DO APP (Módulo específico criado por você)
    ├── __init__.py
    ├── admin.py                   <-- Onde você registra suas tabelas no painel administrativo
    ├── apps.py                    <-- Configurações internas deste módulo específico
    ├── models.py                  <-- Onde você desenha o formato das tabelas do banco de dados
    ├── tests.py                   <-- Onde você escreve testes automatizados para o seu código
    ├── views.py                   <-- A lógica do negócio: processa requisições e envia respostas
    ├── migrations/                <-- Pasta automática: guarda o histórico de mudanças do banco
    │   └── __init__.py
    └── templates/                 <-- Pasta para os seus arquivos HTML
        └── learning_logs/         <-- SUBPASTA COM O NOME DO APP (A boa prática que evita conflitos)
            └── index.html         <-- O seu arquivo HTML limpo
```

---

## Comandos Úteis (Local)

### Criar banco inicial
```bash
python manage.py migrate
```

### Rodar o servidor local
```bash
python manage.py runserver
```

---

## Criando Projeto pelo Docker e Docker Compose

> Nota: Para os comandos abaixo funcionarem, é necessário que os arquivos `docker-compose.yml` e `Dockerfile` já estejam presentes na raiz do projeto.

### 1. Criar arquivos de configuração do Django
```bash
docker compose run --rm web django-admin startproject learninglog .
```

### 2. Subir o contêiner
```bash
docker compose up
```
*(Este comando substitui o tradicional `python manage.py runserver`)*

### 3. Executar as migrations iniciais
```bash
docker compose exec web python manage.py migrate
```

### 4. Criar um novo App
```bash
docker compose exec web python manage.py startapp learning_logs
```

### 5. Criar o modelo de migration (Detectar alterações nos models)
```bash
docker compose exec web python manage.py makemigrations learning_logs
```

### 6. Aplicar a migration do modelo criado no banco de dados
```bash
docker compose exec web python manage.py migrate
```

### 7. Criar login e senha para o painel de administrador (Admin)
```bash
docker compose exec web python manage.py createsuperuser
```

### 8. Abrir o terminal interativo (Shell) do Django
```bash
docker compose exec web python manage.py shell
```
---

# Reutilização de Templates no Django

O Django permite criar templates HTML reutilizáveis, conhecidos como **templates base**. No contexto de páginas que possuem trechos idênticos de HTML, pode-se usar este recurso a fim de promover a reutilização de código e, por consequência, garantir a padronização e a facilidade de manutenção do sistema. 

Por meio das tags de template do Django `{% block content %}`, o código que for definido no template base poderá ser herdado em arquivos que o referenciarem em seu cabeçalho com a tag `{% extends "learning_logs/base.html" %}`, desde que utilizem a tag `{% block content %}` envolvendo o seu conteúdo específico.

---

## Exemplo Prático

### 1. `base.html`
Este é o esqueleto principal da sua aplicação. Ele carrega a estrutura que se repete (como o topo e o menu) e define onde o conteúdo dinâmico será inserido.

```html
<a href="{% url 'index' %}"><h1>Learning Log</h1></a>

{% block content %}
<!-- O conteúdo das outras páginas será injetado aqui -->
{% endblock content %}
```

### 2. `index.html`
Esta é a página específica que herda a estrutura do arquivo base e preenche apenas o bloco de conteúdo que lhe cabe.

```html
{% extends "learning_logs/base.html" %}

{% block content %}
<p>Teste de aplicação</p>
{% endblock content %}
```
