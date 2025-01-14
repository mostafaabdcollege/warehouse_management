import os
from pathlib import Path
from dotenv import load_dotenv
from decouple import config

# تحميل المتغيرات البيئية من ملف .env
load_dotenv()

# تحديد المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح سري لتطبيق Django (يتم تحميله من البيئة أو وضع القيمة الافتراضية)
SECRET_KEY = config('SECRET_KEY', default='#0ej&#7x2$*2+l!e7x2+xwth0b6p49ldz-sz1vt_zi-8u+j7s9')

# وضع التصحيح (تأكد من أنه False في الإنتاج)
DEBUG = config('DEBUG', default=False, cast=bool)

# تحديد المضيفين المسموح بهم
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# إضافة النطاقات الموثوقة لـ CSRF
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='').split(',')
CSRF_TRUSTED_ORIGINS = [f"https://{domain.strip()}" for domain in CSRF_TRUSTED_ORIGINS if domain.strip()]

# إعداد التطبيقات المثبتة
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
    'health_check.db',
    'health_check.cache',
    'health_check.storage',
]

# إعدادات الـ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# تعريف الـ URL root
ROOT_URLCONF = 'warehouse_management.urls'

# إعدادات القوالب (Templates)
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

# تحديد الـ WSGI التطبيق
WSGI_APPLICATION = 'warehouse_management.wsgi.application'

# إعدادات قاعدة البيانات (يمكن تعديلها عند الاستخدام مع قاعدة بيانات أخرى)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# إعدادات التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# إعدادات اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# إعدادات الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'warehouse_management/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# إعدادات ملفات الميديا (الملفات المرفوعة)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# إعدادات الحقول التلقائية (Auto Field)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# تخصيص صفحات الخطأ
HANDLER404 = 'warehouse_management.views.custom_404_view'
HANDLER500 = 'warehouse_management.views.custom_500_view'
