web: gunicorn project.wsgi:application --log-level=debug
worker: celery worker -A project -B --loglevel=INFO --concurrency=5