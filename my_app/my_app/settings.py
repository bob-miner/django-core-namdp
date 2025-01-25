"""
Django settings for my_app project.

Generated by 'django-admin startproject' using Django 1.11.29.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from dotenv import load_dotenv  
import os
import ast

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, '.env')
load_dotenv(ENV_PATH)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'modules.core.apps.CoreConfig',
    'modules.event_management.apps.EventManagementConfig',
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    'corsheaders',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'django.contrib.staticfiles',
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher'
]

# handle import all middlewares

CUSTOM_MIDDLEWARE = [
    # 'modules.core.middlewares.jwt_middleware.JWTMiddleware'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
] + CUSTOM_MIDDLEWARE

MIGRATION_MODULES = {
    'auth': None  # Disable migrations for the auth app
}

ROOT_URLCONF = 'my_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DATABASE', 'XXX'),
        'USER': os.getenv('MYSQL_USERNAME', 'XXX'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD', 'XXX'),
        'HOST': os.getenv('MYSQL_HOST', 'XXX'),
        'PORT': os.getenv('MYSQL_PORT', 'XXX'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

CACHES = {
    "default": {
        "BACKEND": 'django.core.cache.backends.redis.RedisCache',
        "LOCATION": 'redis://{0}:{1}'.format(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT')),
        'KEY_PREFIX': 'myapp'
    }
}

REDIS_HOST = os.getenv('REDIS_HOST', 'XXX')
REDIS_PORT = os.getenv('REDIS_PORT', 'XXX')

EMAIL_ENABLE = os.getenv('EMAIL_ENABLE', False)
EMAIL_HOST = os.getenv('EMAIL_HOST', 'XXX')
EMAIL_PORT = os.getenv('EMAIL_PORT', 'XXX')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', False)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'XXX')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'XXX')
# Keep connection to email server
EMAIL_USE_CONNECTION_POOL = os.getenv('EMAIL_USE_CONNECTION_POOL', False)

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'XXX')
CELERY_ACCEPT_CONTENT = ast.literal_eval(os.getenv('CELERY_ACCEPT_CONTENT', 'XXX'))
CELERY_TASK_SERIALIZER = os.getenv('CELERY_TASK_SERIALIZER', 'XXX')
CELERY_RESULT_SERIALIZER = os.getenv('CELERY_RESULT_SERIALIZER', 'XXX')
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = os.getenv('CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP', False)
CELERY_TIMEZONE = os.getenv('CELERY_TIMEZONE', 'Asia/Ho_Chi_Minh')

CELERY_TASK_ROUTES = {
    'tasks.email.send_mail_event': {'queue': 'email_queue'}
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

JWT_SECRET=os.getenv("JWT_SECRET", "")