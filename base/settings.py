"""
Django settings for base project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!)o*64v60t0nmb-wwe-&zg)+=&eou1^7np)k#h8p(zmxu5-5_k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuario',
    'producto',
    'venta',
    'compra',
    'django_bootstrap5', #pip install django-bootstrap5
    'crispy_forms', #pip install django-crispy-forms
    'crispy_bootstrap5', #pip install crispy-bootstrap5
    'django_bootstrap_icons', #pip install django-bootstrap-icons, pip install django.core.mail
    'dbbackup', #pip install django-dbbackup 
    'django_extensions', # pip install django-extensions

]

CRISPY_ALLOWED_TEMPLATE_PACKS= "bootstrap5"
CRISPY_TEMPLATE_PACK= "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['base/templates'],
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

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS= [
    os.path.join(BASE_DIR,"static"),
    ('node_modules', os.path.join(BASE_DIR, 'node_modules/')),
]
STATIC_ROOT ="/static"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Archivo settings.py

# Configuración de BASE_DIR y otras configuraciones...

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'felminasogamoso@gmail.com'  # Tu dirección de correo electrónico
EMAIL_HOST_PASSWORD = 'vakudacbtlqcybwg'  # Tu contraseña de correo electrónico
EMAIL_USE_TLS = True
# settings.py

# Configuración para las credenciales de OAuth 2.0
GOOGLE_CLIENT_ID = '589772868494-v9in1bhtqtfa76l7efms3hpkrb8oj6kg.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
GOOGLE_REDIRECT_URI = 'http://localhost:8000/google-auth-callback'  # Esta es la URL a la que redirigirá Google después de autorizar la aplicación

# Resto de la configuración de Django...



LOGIN_URL = 'inicio'
LOGIN_REDIRECT_URL = 'index'



BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de django-dbbackup
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {
    'location': BASE_DIR / 'base' / 'backups/'
}

