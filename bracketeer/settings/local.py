from bracketeer.settings.base import *

DEBUG = True
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bracketeer',
        'USER': 'stijn',
        'PASSWORD': None,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
INTERNAL_IPS = ['127.0.0.1']
