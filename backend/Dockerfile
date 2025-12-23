FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*
ENV DJANGO_SETTINGS_MODULE=hello_world.settings.production

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
