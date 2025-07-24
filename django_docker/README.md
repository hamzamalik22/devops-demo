# Django Todo App with Docker (Development Setup)

A simple Django todo application containerized with Docker and PostgreSQL, configured for development.

## Features

- Create and view todo items
- PostgreSQL database
- Docker containerization
- Development setup with Django's runserver
- Hot reloading for code changes
- Debug mode enabled

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

### Development Features

This setup is optimized for development:

- **Hot Reloading**: Code changes are automatically reflected
- **Debug Mode**: Django debug mode is enabled (`DEBUG=True`)
- **Django's runserver**: Uses Django's development server instead of Gunicorn
- **Volume Mounting**: Source code is mounted for live editing
- **No Static Collection**: Static files are served directly by Django

## Project Structure

```
django_docker/
├── Dockerfile              # Docker image configuration (dev setup)
├── docker-compose.yml      # Multi-container setup (dev configuration)
├── .dockerignore          # Files to exclude from Docker build
├── requirements.txt       # Python dependencies
├── entrypoint.sh         # Container startup script (dev optimized)
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

The application uses PostgreSQL. The database configuration is in `myproject/settings.py`:

- **Host**: `db` (Docker service name)
- **Database**: `postgres`
- **User**: `postgres`
- **Password**: `postgres`
- **Port**: `5432`

## Commands

### Docker Commands

```bash
# Build and start (development mode)
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

# Run development server (already running in container)
python manage.py runserver
```

## Environment Variables

- `SECRET_KEY`: Django secret key (required)
- `DEBUG`: Debug mode (True for development)
- `POSTGRES_DB`: Database name
- `POSTGRES_USER`: Database user
- `POSTGRES_PASSWORD`: Database password

## Development vs Production

### Current Setup (Development)
- Uses Django's `runserver` for development
- Debug mode enabled (`DEBUG=True`)
- Source code mounted as volume for hot reloading
- No static file collection (served by Django)
- Runs as root user for easier development

### For Production
To convert to production, you would need to:
1. Use Gunicorn instead of `runserver`
2. Set `DEBUG=False`
3. Collect static files
4. Run as non-root user
5. Use proper environment variables for secrets

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

### Permission Issues

If you encounter permission issues with `entrypoint.sh`:

   ```bash
chmod +x entrypoint.sh
docker-compose build --no-cache
   ```

### Port Already in Use

If port 8000 is already in use, change it in `docker-compose.yml`:

```yaml
ports:
  - "8001:8000"  # Use port 8001 instead
```

### Database Table Errors

If you see "relation does not exist" errors:

```bash
docker-compose exec web python manage.py migrate
``` 