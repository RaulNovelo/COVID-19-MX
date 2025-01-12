# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
import dj_database_url
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2'
    }
}

URL = os.environ.get('DATABASE_URL', None)
DATABASES['default'] = dj_database_url.config(default=URL, conn_max_age=60)
