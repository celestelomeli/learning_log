# Learning Log

Personal journal web application for tracking learning topics and notes.

## Current State (Pre-Production)

**Status:** Development - Not production ready  
**Framework:** Django 4.2.5  
**Python:** 3.11.3  
**Database:** SQLite (dev), PostgreSQL (prod via dj-database-url)

## Features

- User registration and authentication
- Create and manage learning topics
- Add journal entries under topics
- Edit existing entries
- User-specific data isolation (topics/entries owned by creator)

## Architecture

### Apps
- **learning_logs** - Core functionality (Topic/Entry models, CRUD views)
- **users** - Authentication (registration, login/logout)

### Data Models
- `Topic`: text, date_added, owner (FK to User)
- `Entry`: text, date_added, topic (FK to Topic)

### Tech Stack
- Django 4.2.5
- Bootstrap 4 (django-bootstrap4)
- Gunicorn (WSGI server)
- WhiteNoise (static files)
- PostgreSQL adapter (psycopg2)

## Local Setup

```bash
# Activate virtual environment
source ll_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

Visit http://localhost:8000

## Testing

```bash
python manage.py test
```

## Known Issues

**Not production ready** 

## Deployment Config

- `Procfile` - Heroku deployment (gunicorn)
- `runtime.txt` - Python 3.11.5
- Configured for Heroku via django-heroku package

## Project Structure

```
learning_log/          # Django project settings
learning_logs/         # Core app (topics, entries)
users/                 # Authentication app
templates/             # Global templates (404, 500)
staticfiles/           # Collected static files
ll_env/                # Virtual environment
db.sqlite3             # SQLite database (dev)
```

