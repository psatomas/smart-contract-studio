#!/bin/sh
echo "Waiting for backend..."
while ! nc -z backend 8000; do
  sleep 1
done
echo "Backend is up. Starting blockchain..."
uvicorn server:app --host 0.0.0.0 --port 9000 --reload