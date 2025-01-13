import os
from pathlib import Path
from dotenv import load_dotenv
from decouple import config

# Load environment variables from the .env file
load_dotenv()

# Define the base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for Django (loaded from environment or set to default)
SECRET_KEY = config('SECRET_KEY', default='replace-this-secret-key')

# Debug mode (loaded from environment, default is False)
DEBUG = config('DEBUG', default=False, cast=bool)

# Allowed hosts for the app (loaded from environment)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# CSRF trusted origins (loaded from environment, with 'https://' prefix)
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='').split(',')
CSRF_TRUSTED_ORIGINS = [f"https://{domain.strip()}" for domain in CSRF_TRUSTED_ORIGINS if domain.strip()]

# Installed apps for the Django project
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inventory',
    'bootstrap5',
    'django_extensions',
    'health_check',
]

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'warehouse_management.urls'

# Template configuration
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

# WSGI application for deployment
WSGI_APPLICATION = 'warehouse_management.wsgi.application'

# Database configuration (using SQLite for simplicity)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation rules
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization and time zone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JS, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'warehouse_management/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default auto field for models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom error pages
HANDLER404 = 'warehouse_management.views.custom_404_view'
HANDLER500 = 'warehouse_management.views.custom_500_view'