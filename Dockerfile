# Usa a imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Impede que o Python grave arquivos .pyc no disco
ENV PYTHONDONTWRITEBYTECODE=1
# Impede que o Python faça buffer na saída padrão e de erro
ENV PYTHONUNBUFFERED=1

# Instala dependências do sistema se necessário
RUN apt-get update && apt-get install -y build-essential

# Atualiza o pip e instala as dependências do Python
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o restante do código do projeto para o contêiner
COPY . /app/