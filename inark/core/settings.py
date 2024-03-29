# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from pathlib import Path
import os, environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

# BASE_DIR :  /usr/src/app
# CORE_DIR :  /usr/src/app
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = Path(__file__).resolve().parent.parent
# print("BASE_DIR : ",BASE_DIR)
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print("CORE_DIR : ",CORE_DIR)
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='S#perS3crEt_007')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env('DEBUG')
DEBUG = int(os.environ.get("DEBUG", default=1))

# Assets Management
ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets') 
print("ASSETS_ROOT:",ASSETS_ROOT)

# load production server from .env
# ALLOWED_HOSTS        = ['localhost', '127.0.0.1', 'www.arkwith.com', 'arkwith.com',              env('SERVER', default='127.0.0.1') ]
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
print("ALLOWED_HOSTS=",ALLOWED_HOSTS)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_TRUSTED_ORIGINS = ['http://localhost', 'http://127.0.0.1', 'https://' + env('SERVER', default='127.0.0.1') ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'widget_tweaks',

    't_ocr', 
    'g_ocr', 
    'apps.home'  # Enable the inner home (home)
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.context_processors.cfg_assets_root',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, 'db.sqlite3')),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

# if os.environ.get('DB_ENGINE') and os.environ.get('DB_ENGINE') == "mysql":
#     DATABASES = { 
#       'default': {
#         'ENGINE'  : 'django.db.backends.mysql', 
#         'NAME'    : os.getenv('DB_NAME'     , 'appseed_db'),
#         'USER'    : os.getenv('DB_USERNAME' , 'appseed_db_usr'),
#         'PASSWORD': os.getenv('DB_PASS'     , 'pass'),
#         'HOST'    : os.getenv('DB_HOST'     , 'localhost'),
#         'PORT'    : os.getenv('DB_PORT'     , 3306),
#         }, 
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': 'db.sqlite3',
#         }
#     }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
print("STATIC_ROOT=",STATIC_ROOT)
# STATIC_ROOT = BASE_DIR / "staticfiles"

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
)


#############################################################
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(CORE_DIR, 'mediafiles')
# MEDIA_ROOT = BASE_DIR / "mediafiles"
#############################################################

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'