FROM python:3.13-alpine3.21 AS flask-rest-api-template
LABEL authors="leo Fornoff"

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=app.main
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PROMETHEUS_MULTIPROC_DIR="/tmp/prometheus_multiproc_dir"

WORKDIR /app

# Installation of the necessary packages
RUN apk update && apk add --no-cache \
    build-base \
    cmake \
    pkgconf \
    mariadb-dev \
    libffi-dev \
    openssl-dev \
    linux-headers \
    && rm -rf /var/cache/apk/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy of application files
COPY app ./app
COPY run.py .

EXPOSE 5000

CMD ["sh", "-c", "gunicorn -w $(nproc) -t 120 -b 0.0.0.0:5000 run:app --log-config app/config/log.conf"]
