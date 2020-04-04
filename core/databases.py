# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
import dj_database_url
import os
from django.conf import settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}

# URL = os.environ.get('DATABASE_URL', None)
# DATABASES['default'] = dj_database_url.config(default=URL, conn_max_age=60)
