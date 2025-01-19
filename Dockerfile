# Étape de développement
FROM python:3.9-slim AS development

# Installer les outils nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Exposer le port pour le développement
EXPOSE 5000
ENV FLASK_ENV=development
CMD ["python", "run.py", "--host=0.0.0.0"]

# Étape de production
FROM python:3.9-slim AS production

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Exposer le port pour la production
EXPOSE 5000
CMD ["python", "run.py", "--host=0.0.0.0"]
