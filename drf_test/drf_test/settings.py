"""
Django settings for drf_test project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vcsv1mz$h58j=dmi!2c8z7u98okzbzec*7z4n_h817q+wz^#bk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booktest',
    'rest_framework',
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

ROOT_URLCONF = 'drf_test.urls'

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

WSGI_APPLICATION = 'drf_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'drf_test',
        'USER': 'root',
        'PASSWORD': '970220',
        'HOST': '127.0.0.1',
        'PORT': 3306
}
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


REST_FRAMEWORK = {
    # 1.认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # session认证   仅使用session认证方式
        'rest_framework.authentication.SessionAuthentication',
        # 基本认证(仅了解)
        # 'rest_framework.authentication.BasicAuthentication'
    ),
    # 2.权限
    'DEFAULT_PERMISSION_CLASSES': (
        # 允许所有人进行访问
        'rest_framework.permissions.AllowAny',
        # 此处设置全局权限控制方式为：仅允许通过认证的用户访问
        # 'rest_framework.permissions.IsAuthenticated',
    ),
    # 3.限流
    # 3.1分别限流
    # 针对匿名用户和认证通过用户分别进行限流控制
    # 'DEFAULT_THROTTLE_CLASSES': (
    #     # 针对未登录(匿名)用户的限流控制类
    #     'rest_framework.throttling.AnonRateThrottle',
    #     # 针对登录(认证通过)用户的限流控制类
    #     'rest_framework.throttling.UserRateThrottle'
    # ),
    # # 指定限流频次
    # 'DEFAULT_THROTTLE_RATES': {
    #     # 认证用户的限流频次
    #     'user': '5/minute',
    #     # 匿名用户的限流频次
    #     'anon': '3/minute',
    # },
    # 3.2 统一限流
    # 针对匿名用户和认证用户进行统一的限流控制
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.ScopedRateThrottle',
    ),
    # 指定限流频次选择项
    'DEFAULT_THROTTLE_RATES': {
    # 注：此处的限流频次选择项的名字是自己起的，只要不叫user和anon即可
        'upload': '3/minute',
        'contacts': '5/minute'
    },
    # 4.分页
    # 设置DRF框架所使用的全局分页类
    "DEFAULT_PAGINATION_CLASS":"rest_framework.page.PageNumberPagination",
    # # 指定页容量为2
    # "PAGE_SIZE": 2
}