"""
Desarollador por @d4n7.dev

"""
from pathlib import Path
import os
from decouple import config, RepositoryEnv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#ENV_PATH = BASE_DIR.parent / '.env'  
#env_config = Config(repository=RepositoryEnv(str(ENV_PATH)))

MEDIA_URL = 'sistemas_cuentas/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'sistemas_cuentas/static/')


SECRET_KEY = 'django-insecure-96(7#*1nkbz)-ymkrr!z$5*m1g*(xfmy37tq+a**za_nn9qq$o'

DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    #'unfold',  
    #"unfold.contrib.filters",  # optional, if special filters are needed
    #"unfold.contrib.forms",  # optional, if special form elements are needed
    #"unfold.contrib.inlines",  # optional, if special inlines are needed
    #"unfold.contrib.import_export",  # optional, if django-import-export package is used
    #"unfold.contrib.guardian",  # optional, if django-guardian package is used
    #"unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion_identidades',
    'django_celery_results',
    'django_celery_beat',
    'iam',
    'rest_framework',
    'django_json_widget',
    'gestion_supervisor',
    'gestion_organizacion',
  
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

ROOT_URLCONF = 'iam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'iam.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




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

###CONFIGURACION DE CORREO
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')


LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True



STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

UNFOLD = {
    "SITE_TITLE": "Panel Admin - d4n7.dev",
    "SITE_HEADER": "Identidades informaticas",
    "SHOW_HISTORY": True,
    "PRIMARY_COLOR": "blue",
    "MENU": [
        {
            "type": "title",
            "label": "Gestión",
        },
        {
            "type": "model",
            "label": "Usuarios",
            "model": "auth.User",
            "icon": "user",
        },
        {
            "type": "model",
            "label": "Grupos",
            "model": "auth.Group",
            "icon": "users",
        },
    ],
}

