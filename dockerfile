# Dockerfile
FROM python:3.13.3

# Cria diretório da aplicação
WORKDIR /app

# Copia os arquivos da API
COPY ./app ./app
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta
EXPOSE 8000

# Roda o servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
