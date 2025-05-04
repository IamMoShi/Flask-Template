# Using an official image of Python
FROM python:3.13 as flask-rest-api-template
LABEL authors="leo Fornoff"

# Definition of environmental variables
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=app.main
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Defines the Docker's work file
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app in /app /app
COPY app ./app

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-t", "120", "-b", "0.0.0.0:5000", "app.main:app"]
