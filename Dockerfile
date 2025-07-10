# Use official Python image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /var/www/html

# Install dependencies
COPY requirements.txt /var/www/html/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /var/www/html/

# Collect static files (if you use collectstatic)
RUN python manage.py collectstatic --noinput

# Expose port for Gunicorn
EXPOSE 8000

# Start Gunicorn
CMD ["gunicorn", "cheferv1.wsgi:application", "--bind", "0.0.0.0:8000"]
