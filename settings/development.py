from .base import *

DEBUG = True


SECRET_KEY = 'django-insecure-x$@aob*&splp(j*e5o2cr(s2sp4bkv+3+8(k5^wjcip6y2t$2!'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'
        
    }
}


