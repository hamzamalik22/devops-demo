# Django Todo App with Docker

A simple Django todo application containerized with Docker and PostgreSQL.

## Features

- Create and view todo items
- PostgreSQL database
- Docker containerization
- Production-ready setup with Gunicorn

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd django_docker
   ```

2. **Build and start the containers**:
   ```bash
   docker-compose up --build
   ```

3. **Access the application**:
   - Todo app: http://localhost:8000
   - Admin interface: http://localhost:8000/admin

### Development

For development with hot reloading:

```bash
# Run in development mode
docker-compose -f docker-compose.yml up --build
```

### Production Deployment

1. **Set environment variables**:
   Create a `.env` file or set environment variables:
   ```bash
   SECRET_KEY=your-secure-secret-key
   DEBUG=False
   ```

2. **Run in production mode**:
   ```bash
   docker-compose up -d
   ```

## Project Structure

```
django_docker/
├── Dockerfile              # Docker image configuration
├── docker-compose.yml      # Multi-container setup
├── .dockerignore          # Files to exclude from Docker build
├── requirements.txt       # Python dependencies
├── entrypoint.sh         # Container startup script
├── manage.py             # Django management script
├── myproject/            # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todo/                 # Todo app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
└── db.sqlite3           # SQLite database (development)
```

## Database

The application uses PostgreSQL in production. The database configuration is in `myproject/settings.py`:

- **Host**: `db` (Docker service name)
- **Database**: `postgres`
- **User**: `postgres`
- **Password**: `postgres`
- **Port**: `5432`

## Commands

### Docker Commands

```bash
# Build and start
docker-compose up --build

# Start in background
docker-compose up -d

# Stop containers
docker-compose down

# View logs
docker-compose logs

# Access Django shell
docker-compose exec web python manage.py shell

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser
```

### Django Commands

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver
```

## Environment Variables

- `SECRET_KEY`: Django secret key (required)
- `DEBUG`: Debug mode (True/False)
- `POSTGRES_DB`: Database name
- `POSTGRES_USER`: Database user
- `POSTGRES_PASSWORD`: Database password

## Security Notes

- Change the default `SECRET_KEY` in production
- Update `ALLOWED_HOSTS` in `settings.py` for production
- Use environment variables for sensitive data
- Consider using Docker secrets for production deployments

## Troubleshooting

### Database Connection Issues

If the web container can't connect to the database:

1. Check if the database container is running:
   ```bash
   docker-compose ps
   ```

2. Check database logs:
   ```bash
   docker-compose logs db
   ```

3. Wait for the database to be ready (the entrypoint script handles this)

### Static Files Not Loading

If static files aren't loading:

1. Ensure static files are collected:
   ```bash
   docker-compose exec web python manage.py collectstatic
   ```

2. Check if Whitenoise is properly configured in settings

### Port Already in Use

If port 8000 is already in use, change it in `docker-compose.yml`:

```yaml
ports:
  - "8001:8000"  # Use port 8001 instead
``` 