import os
from datetime import timedelta

from . import secret
from easy_thumbnails.conf import Settings as thumbnail_settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = secret.SECRET_KEY

SITE_NAME = 'Hevent'
DEBUG = secret.DEBUG
LOCAL = secret.LOCAL
DOMAIN = secret.DOMAIN

ALLOWED_HOSTS = ['.' + DOMAIN, DOMAIN]

CORS_ORIGIN_WHITELIST  =  [
    "http://localhost:3000" ,
    "http://holytribe.localhost:3000" ,
]

COMMON_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.postgres',

    'adminsortable2',
    'debug_toolbar',
    'easy_thumbnails',
    'image_cropping',
    'rest_framework',
    'corsheaders',
]

SHARED_APPS = [
    'django_tenants',
    'apps.guilds',
    'apps.users',
    'apps.pw',
    'apps.chars',
    'apps.help',
] + COMMON_APPS

TENANT_APPS = [
    'apps.compositions',
    'apps.constrforms',

] + COMMON_APPS
INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

TENANT_MODEL = "guilds.Guild"
TENANT_DOMAIN_MODEL = "guilds.Domain"
AUTH_USER_MODEL = 'users.User'

ROOT_URLCONF = 'system.urls_tenants'
PUBLIC_SCHEMA_URLCONF = 'system.urls_public'


AUTHENTICATION_BACKENDS = [
    'apps.users.backends.UserBackend'
]
if not LOCAL:
    SESSION_COOKIE_DOMAIN = '.' + DOMAIN

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]
SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.guilds.context_processors.main',
            ],
        },
    },
]

WSGI_APPLICATION = 'system.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': secret.DATABASE['NAME'],
        'USER': secret.DATABASE['USER'],
        'PASSWORD': secret.DATABASE['PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

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


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = secret.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = secret.EMAIL_HOST_PASSWORD
EMAIL_PORT = 587 if EMAIL_USE_TLS else 27
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets")
]

DOMAIN_DIR = f'var/www/domains/{DOMAIN}/'
CURRENT_DIR = BASE_DIR if LOCAL else DOMAIN_DIR

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(CURRENT_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(CURRENT_DIR, 'media')


if DEBUG:
    TEMPLATES[0]['OPTIONS']['context_processors'].insert(0, 'django.template.context_processors.debug')
    MIDDLEWARE.insert(1, 'debug_toolbar.middleware.DebugToolbarMiddleware')

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 200,
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=300),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'
