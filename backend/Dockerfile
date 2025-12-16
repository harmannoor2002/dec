FROM python:3.11-slim
## Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1 \   
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
<<<<<<< HEAD
#UPDATE PACKAGE LIST AND TOOL INSTALL LARY GA 
#TOOL NEED TO compile python packages
#tool need to download from internet
#clean up to reduce image size
=======
>>>>>>> fc064dcd2abebd4ac76312dfd63b452d50c5d06d
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

<<<<<<< HEAD

COPY . /app/

# tell Django to use the production settings
=======
# Copy all backend source code
COPY . /app/

# Set environment variable for Django
>>>>>>> fc064dcd2abebd4ac76312dfd63b452d50c5d06d
ENV DJANGO_SETTINGS_MODULE=hello_world.settings.production

# Expose the Django port
EXPOSE 8000

<<<<<<< HEAD
#start the Django server to it can aceess outside the container 
=======
# Command to run Django development server
>>>>>>> fc064dcd2abebd4ac76312dfd63b452d50c5d06d
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]






