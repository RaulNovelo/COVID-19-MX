import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm9ns176@$mjyin2fliqu81svm6$038#f02u+rg0&pffcz-4mm0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', 1))
ENV = os.environ.get('ENV', None)
ALLOWED_HOSTS = ['*']
