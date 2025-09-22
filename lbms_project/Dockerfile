# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Set environment variables for a secure and optimized app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies needed for database connectors
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies, including gunicorn and the database driver
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port on which the app will run
EXPOSE 8000

# Run Django migrations and start the Gunicorn web server
CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 lbms_project.wsgi"]