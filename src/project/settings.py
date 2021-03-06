# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'ZZZSECRET'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'apps.zzzzz'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DJANGO_DATABASE_ENGINE"),
        'HOST': os.environ.get("DJANGO_DATABASE_HOST"),
        'NAME': os.environ.get("DJANGO_DATABASE_NAME"),
        'USER': os.environ.get("DJANGO_DATABASE_USER"),
        'PASSWORD': os.environ.get("DJANGO_DATABASE_PASSWORD")
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis:6379',
        'OPTIONS': {
            'DB': 1,
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        }
    }
}

SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = 'redis'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 1
SESSION_REDIS_PREFIX = 'zzzzz'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('DJANGO_STATIC_ROOT', '/static')
MEDIA_ROOT = os.environ.get('DJANGO_MEDIA_ROOT', '/media')

LOGGING = {

    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        # 'fluentd': {
        #     '()': 'fluent.handler.FluentRecordFormatter',
        #     'format': {
        #         'sys_name': '%(name)s',
        #         'level': '%(levelname)s',
        #         'source_host': '%(hostname)s',
        #         'source': '%(module)s',
        #     }
        # },
        'console': {
            'format': '[%(module)s].%(levelname)s %(message)s'
        }
    },

    'handlers': {
        # 'fluentd': {
        #     'level': 'INFO',
        #     'class': 'fluent.handler.FluentHandler',
        #     'formatter': 'fluentd',
        #     'tag': 'django.log',
        #     'host': os.environ.get('DJANGO_FLUENTD_HOST'),
        #     'port': 24224,
        # },
        'logstash': {
            'level': 'INFO',
            'class': 'logstash.TCPLogstashHandler',
            'host': os.environ.get('DJANGO_LOGSTASH_HOST'),
            'port': os.environ.get('DJANGO_LOGSTASH_PORT'),
            'version': 1,
            'message_type': 'logstash',
            'fqdn': True,
            'tags': ['django'],
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
    },

    'loggers': {
        'app.logger': {
            'handlers': ['logstash', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['logstash', 'console'],
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['logstash', 'console'],
            'level': 'INFO',
        }
    },
}

if os.environ.get('APP_ENV') == 'test':
    from .test_settings import *  # NOQA
