FROM python:3.11-slim
## Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1 \   
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
#UPDATE PACKAGE LIST AND TOOL INSTALL LARY GA 
#TOOL NEED TO compile python packages
#tool need to download from internet
#clean up to reduce image size
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . /app/

# tell Django to use the production settings
ENV DJANGO_SETTINGS_MODULE=hello_world.settings.production

EXPOSE 8000

#start the Django server to it can aceess outside the container 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]






