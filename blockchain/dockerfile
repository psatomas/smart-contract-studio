# Dockerfile do backend
FROM python:3.13-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y netcat-openbsd
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]