# -*- coding: utf-8 -*-

from istari.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cm!p3n14s8k)cg67(6ws6(ec@37f4clz!3z#z-8i^%j-%(0g%9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

LOCAL_APPS = ()

INSTALLED_APPS += LOCAL_APPS

LOCAL_MIDDLEWARES = ()

MIDDLEWARE_CLASSES += LOCAL_MIDDLEWARES


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
