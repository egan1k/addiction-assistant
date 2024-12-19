from pathlib import Path
import os
from back.settings.django_environ import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.postgres",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "django_extensions",
    "django_filters",

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'back.urls'

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

WSGI_APPLICATION = 'back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": "",
    }
}

# if env("REDIS_URL"):
#     redbeat_redis_url = os.environ.get("REDIS_URL", "redis://redis:6379") + "/1"
#     use_ssl = redbeat_redis_url.startswith("rediss://")
#     if use_ssl:
#         CACHES = {
#             "default": {
#                 "BACKEND": "django_redis.cache.RedisCache",
#                 "LOCATION": os.environ.get("REDIS_URL"),
#                 "OPTIONS": {
#                     "CLIENT_CLASS": "django_redis.client.DefaultClient",
#                     "CONNECTION_POOL_KWARGS": {"ssl_cert_reqs": None},
#                 },
#             }
#         }
#     else:
#         CACHES = {
#             "default": {
#                 "BACKEND": "django_redis.cache.RedisCache",
#                 "LOCATION": env("REDIS_URL"),
#                 "OPTIONS": {
#                     "CLIENT_CLASS": "django_redis.client.DefaultClient",
#                 },
#             },
#         }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# AUTH_USER_MODEL = "main.User"


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

DATE_INPUT_FORMATS = [
    "%m/%d/%Y",
    "%Y-%m-%d",
    "%m/%d/%y",
    "%b %d %Y",
    "%b %d, %Y",
    "%d %b %Y",
    "%d %b, %Y",
    "%B %d %Y",
    "%B %d, %Y",
    "%d %B %Y",
    "%d %B, %Y",
]

DATE_FORMAT = "m/d/Y"
DATETIME_FORMAT = "m/d/Y P"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

