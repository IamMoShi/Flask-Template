# Development
FROM python:3.13 AS development

# Tools
RUN apt-get update && apt-get install pkg-config python3-dev default-libmysqlclient-dev build-essential -y
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Development port
EXPOSE 5000
ENV FLASK_ENV=development
CMD ["python", "run.py"]

# Production
FROM python:3.13 AS production

# Tools
RUN apt-get update && apt-get install pkg-config python3-dev default-libmysqlclient-dev build-essential -y
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Production port
EXPOSE 5000
CMD ["python", "run.py"]
