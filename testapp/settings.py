from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "N6PyDWO6hrRaBfCYlXUPt13JEATKA+mufYYpkUV582U3aslb2xoQK2jhiXGUxH1DzGfD1RtFub1X+nvn+OG8YQ=="

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("APP_DEBUG", False)

# SECURE_SSL_REDIRECT = os.getenv("APP_SECURE_SSL_REDIRECT", True)
SESSION_COOKIE_SECURE = os.getenv("APP_SESSION_COOKIE_SECURE", True)
CSRF_COOKIE_SECURE = os.getenv("APP_CSRF_COOKIE_SECURE", True)

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ') or []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "posts",
    "users",
    "comments",
    "api",
    "rest_framework",
    "dashboard",
    'django_vite_plugin',
    'django_ckeditor_5',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "testapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
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

WSGI_APPLICATION = "testapp.wsgi.application"


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

STATIC_URL = "static/"
MEDIA_URL = "media/"
STATICFILES_DIRS = [BASE_DIR / "static"]

DJANGO_VITE_PLUGIN = {
    "BUILD_DIR": "static/build",
    "BUILD_URL_PREFIX": "/" + STATIC_URL + "build",
    "DEV_MODE": False,
}


STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "login"
LOGOUT_REDIRECT_URL = "login"


# CKEditor Settings
# CKEDITOR_5_CUSTOM_CSS = BASE_DIR / "src/editor.css"
CKEDITOR_5_CONFIGS = {
  'default': {
      'toolbar': ['heading', '|', 'bold', 'italic', 'link', '|',
                  'bulletedList', 'numberedList', '|', 'blockQuote', 'imageUpload', ],
  },
}