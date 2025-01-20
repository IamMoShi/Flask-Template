# Development
FROM python:3.13 AS development
# Tools
RUN apt-get update && apt-get install pkg-config python3-dev default-libmysqlclient-dev build-essential -y
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Development port
EXPOSE 5000
CMD ["python", "run.py"]

# Production
FROM python:3.13 AS production

# Tools
RUN apt-get update && apt-get install pkg-config python3-dev default-libmysqlclient-dev build-essential -y
WORKDIR /app
COPY requirements.txt requirements.txt
COPY flask_app flask_app
RUN pip install --no-cache-dir -r requirements.txt
# Production port
EXPOSE 8000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0", "flask_app:prod()"]

# Unit tests
FROM python:3.13 AS unit
# Tools
RUN apt-get update && apt-get install pkg-config python3-dev default-libmysqlclient-dev build-essential -y
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "Tests/unit-run.py"]

# Integration tests
FROM python:3.13 AS integration
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "Tests/integration-run.py"]

# All tests
FROM python:3.13 AS all-tests
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["pytest", "Tests/"]