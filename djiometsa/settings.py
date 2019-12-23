
import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

CLEF_NAME = 'clef.json'
CLEF_REL_PATH = 'djiometsa/data/{}'
ROOT_CLEF = '/home/data/{}'
CLEF_REL_PATH = os.path.join(BASE_DIR, CLEF_REL_PATH)


def dev_settings():
    return 'runserver' in sys.argv


if dev_settings():
    CLEF_PATH = os.path.join(BASE_DIR, CLEF_REL_PATH.format(CLEF_NAME))
else:
    CLEF_PATH = ROOT_CLEF.format(CLEF_NAME)


clef = {}
with open(CLEF_PATH, mode='r') as j_clef:
    clef.update(json.load(j_clef))


if dev_settings():
    try:
        from djiometsa.dev_settings import *
    except ImportError:
        sys.exit('Error: Missing dev_settings module')

    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False
    SECURE_SSL_REDIRECT = False
else:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    ALLOWED_HOSTS = clef['allowed_hosts']


SECRET_KEY = clef['django_key']
GOOGLE_RECAPTCHA_KEY = clef['recaptcha']


# Email settings
EMAIL_BACKEND = clef['email_backend']
EMAIL_HOST = clef['email_host']
EMAIL_PORT = 465
EMAIL_HOST_USER = clef['email_host_user']
EMAIL_HOST_PASSWORD = clef['email_host_pass']
EMAIL_USE_TLS = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'resume',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djiometsa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djiometsa.wsgi.application'

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "resume/static"),
# ]
STATIC_ROOT = os.path.join(BASE_DIR, "resume/static")
