"""
Django settings for shopifyapp project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from secret import SHOPIFY_APP_API_KEY, SHOPIFY_APP_API_SECRET
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kjzycoyzif(t9@t%16!jw-xdt%s4tdpqnja4xo5(fz7y6q2*o('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shopify_app',
    'shopify_auth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'shopifyapp.urls'

WSGI_APPLICATION = 'shopifyapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'auth_app.AuthAppShopUser'

# Configure Shopify Application settings
SHOPIFY_APP_NAME = 'Shopify App'
SHOPIFY_APP_API_KEY = SHOPIFY_APP_API_KEY
SHOPIFY_APP_API_SECRET = SHOPIFY_APP_API_SECRET
SHOPIFY_APP_API_SCOPE = ['read_products', 'read_orders']
SHOPIFY_APP_IS_EMBEDDED = True
SHOPIFY_APP_DEV_MODE = False

# Use the Shopify Auth authentication backend as the sole authentication backend.
AUTHENTICATION_BACKENDS = (
    'shopify_auth.backends.ShopUserBackend',
)

# Add the Shopify Auth template context processor to the list of processors.
# Note that this assumes you've defined TEMPLATE_CONTEXT_PROCESSORS earlier in your settings.
TEMPLATE_CONTEXT_PROCESSORS += (
    'shopify_auth.context_processors.shopify_auth',
)

# Use the Shopify Auth user model.
AUTH_USER_MODEL = 'shopify_app.ShopifyAppShopUser'

# Set the login redirect URL to the "home" page for your app (where to go after logging on).
LOGIN_REDIRECT_URL = '/'
