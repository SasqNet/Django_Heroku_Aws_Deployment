#Import Security details from base.py
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#*(&5yfmrt-^d8bj2gt*$m**(euas93gq8qf=flygi=xkam2i3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / 'staticfiles'                           #os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'media/' 

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')