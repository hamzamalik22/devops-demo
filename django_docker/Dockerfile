# Use Python 3.11 slim image as the base image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and to enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container to /app
WORKDIR /app

# Install system dependencies required for building and running Python packages and PostgreSQL client
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        gcc \
        python3-dev \
        musl-dev \
        libpq-dev \
        netcat-traditional \
    && rm -rf /var/lib/apt/lists/*  # Clean up apt cache to reduce image size

# Copy Python dependencies file to the container
COPY requirements.txt .
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh

# Expose port 8000 for the Django development server
EXPOSE 8000

# Set the entrypoint script to run on container start
ENTRYPOINT ["./entrypoint.sh"]

# Default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 