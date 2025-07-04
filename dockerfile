FROM python:3.13.3


WORKDIR /app

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY ./app ./app

# Expõe a porta
EXPOSE 8000

# Roda o servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
