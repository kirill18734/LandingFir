"""
Django settings for project_fit project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# глобальные настройки для нашего проекта
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# полный путь к нашему проекту
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
# секретный ключ
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_i)mw)*@0++gggaj(v3()73t#10f!r9tga!l3_!9b5$4!m-$wv'
# предназначено для отображения ошибок на самом сайте  (True - показывает, False - не показывает)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# это переменная в которой будет доменные имена , на который нам будет разрешено опубликовать данный сайт
# пример (itproget.com)
ALLOWED_HOSTS = []

# Application definition
# хранит набор всех установленных приложений, которые у нас уже установлены (
INSTALLED_APPS = [
    # эти приложения по умолчанию

    'django.contrib.admin',  # это для администратора приложения
    'django.contrib.auth',  # это для администратора приложения
    'django.contrib.contenttypes',  # работа с типами данных
    'django.contrib.sessions',  # работа с сессии
    'django.contrib.messages',  # работа с сообщениями
    'django.contrib.staticfiles',  # статический файлы
    # это наши утсановленый приложения
    'main',
]
# сдесь записаны все промежуточные по
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # плагин который обеспечиет безопасность внутри проекта
    'django.contrib.sessions.middleware.SessionMiddleware',  # плагин который обеспечиет безопасность сессии
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # плагин который обеспечиет поддержку csrf токена
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # клас коорый обеспечиет безопасную авторизацию внутри проекта
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# файл url , который будет использоваться для всего проекта
ROOT_URLCONF = 'project_fit.urls'

# какие шаблоны будут использоваться для всех проекта

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
# указывает что мы используем wsgi, с помощью этой технологии мы сможем выгрузить наш сайт на сервер
WSGI_APPLICATION = 'project_fit.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# база данных с которой мы работаем
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/
# язык для всего нашего проекта
LANGUAGE_CODE = 'en-us'
# временная зона для нашего проекта
TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]