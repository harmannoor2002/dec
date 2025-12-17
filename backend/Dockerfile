FROM python:3.11-slim

# Prevent Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

<<<<<<< HEAD
# Copy all backend source code
=======
# Copy backend source code
>>>>>>> b3cfc5f (Fix Dockerfile merge conflicts)
COPY . /app/

# Set environment variable for Django
ENV DJANGO_SETTINGS_MODULE=hello_world.settings.production

# Expose the Django port
EXPOSE 8000

<<<<<<< HEAD
# Command to run Django server
=======
# Start the Django server
>>>>>>> b3cfc5f (Fix Dockerfile merge conflicts)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
