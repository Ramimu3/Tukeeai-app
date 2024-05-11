"""
Django settings for AIDTdjango project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from . info import *
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@h!wy$+@fy@!jkg=3g^%gjfeh%a4z14oq$87l6p%-1(ogyv$3%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['tukeeai-922147af33a3.herokuapp.com', 'tukeeai.com', 'www.tukeeai.com', '127.0.0.1']





# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    'django.contrib.sites',
    "myapp",
    "authentication",
    "django_celery_results",
    'ninja',
    'celery_progress',
    'django.contrib.messages',
    'api',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'stripe_integration',
    'corsheaders',


]


MIDDLEWARE = [
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',

]
STATIC_URL = "/static/"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'static'),
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',  # Replace with your Svelte frontend's URL
]

ROOT_URLCONF = "AIDTdjango.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'frontend', 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "AIDTdjango.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CELERY_BROKER_URL = 'amqp://localhost'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'

DATA_UPLOAD_MAX_MEMORY_SIZE = 31457280  # 30MB


CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Strict'

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    
]


DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # For testing purposes

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '588136752975-vmtenmsrah1buukuhcb4gnr7r5ne120e.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    },
    'github': {
        'APP': {
            'client_id': 'e024677e422606095a8c',
            'secret': '74f20c4c1fbf41a9f969c395811dc099df008eaa',
            'key': ''
        }
    },
    'facebook': {
        'APP': {
            'client_id': 'your-facebook-client-id',
            'secret': 'your-facebook-client-secret',
            'key': ''
        }
    }
}

SESSION_COOKIE_SECURE = True  # Use with HTTPS only

STRIPE_PUBLISHABLE_KEY = 'pk_test_51NaOxiA550ilgONrAqQ6opcdwWJHKuWy72atW0DkFfAHMheeybsTV7dZGgnjAqWdUZZIXmgVNyyrOsQLwG1kzzXb00wqGXGRYv'
STRIPE_SECRET_KEY_TEST= 'sk_test_51NaOxiA550ilgONrqKLr5AlFH4GC4af8MJYovN5RDeSqX23ugzu9pmaSflmMviB719prf8d3O0d0uHIceilGdmuc00DVl8b3nF'
REDIRECT_DOMAIN = 'http://localhost:8000'  # Replace with your domainSTRIPE_WEBHOOK_SECRET_TEST = 'your_test_webhook_secret'
STRIPE_WEBHOOK_SECRET_TEST = 'whsec_66d6998db577cf061510cb2e174178b063432c6cf041e14a311566a71800881c'
STRIPE_SECRET_KEY= 'sk_test_51NaOxiA550ilgONrqKLr5AlFH4GC4af8MJYovN5RDeSqX23ugzu9pmaSflmMviB719prf8d3O0d0uHIceilGdmuc00DVl8b3nF'
STRIPE_SUBSCRIPTION_PRICE_ID = 'price_1P2txfA550ilgONrcjyBBM6u'
STRIPE_PRICE_ID = 'price_1P6jxQA550ilgONrmCpAbYyx'
CSRF_COOKIE_NAME = 'csrftoken'
CSRF_HEADER_NAME = 'X-CSRFToken'
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True 
SOCIAL_AUTH_GOOGLE_OAUTH2_CALLBACK_URL = 'https://www.tukeeai.com/accounts/google/login/callback/'
SOCIALACCOUNT_LOGIN_ON_GET=True
SOCIALACCOUNT_ADAPTER = 'myapp.adapters.custom_adapter.SocialAccountAdapter'



SITE_ID = 1
