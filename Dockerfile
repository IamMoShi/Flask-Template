FROM python:3.13-alpine AS flask_app_base
WORKDIR /app

RUN apk update && apk add --no-cache \
    gcc \
    g++ \
    musl-dev \
    libffi-dev \
    python3-dev \
    mariadb-connector-c-dev \
    build-base \
    mariadb-dev

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# production stage
FROM flask_app_base AS production
COPY flask_app flask_app
COPY wsgi.py wsgi.py
EXPOSE 8000
CMD ["gunicorn", "-c", "flask_app/config/gunicorn_config.py", "wsgi:app"]

# development stage
FROM flask_app_base AS development
COPY . .
EXPOSE 5000
CMD ["python", "run.py"]

# unittest stage
FROM flask_app_base AS unittest
COPY . .
CMD ["python", "Tests/unit-run.py"]

# integrationtest stage
FROM flask_app_base AS integration
COPY . .
CMD ["python", "Tests/integration-run.py"]