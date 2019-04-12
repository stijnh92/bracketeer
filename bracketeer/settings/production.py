from bracketeer.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USERNAME'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

SECRET_KEY = os.environ['SECRET_KEY']

INTERNAL_IPS = ['127.0.0.1']

STATIC_ROOT = os.environ['STATIC_ROOT']
