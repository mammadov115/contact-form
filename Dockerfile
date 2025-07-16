# Dockerfile
FROM python:3.12-slim

# Working directory
WORKDIR /app

# Install GCC compiler
# This is necessary for building some Python packages that require compilation
RUN apt-get update && apt-get install -y gcc

# Copy all files from the current directory to the working directory
COPY . . 

# Install Poetry
RUN pip install poetry==2.1.3

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && poetry install --only main

# Django runserver command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=config.settings.prod"]
