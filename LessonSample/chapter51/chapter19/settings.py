#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Django settings for chapter19 project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# 获取项目的根目录，即顶层的那个chapter19目录，不是当前settings.py所在的chapter19目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 秘钥串
SECRET_KEY = '!56%3g95p4my$^-^qfmw*amricupjebxsf_s8!%_+0^p)m_aq+'

# 是否开启调试
DEBUG = True
# 允许访问的域名，生产环境必须设置
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# 当前项目安装的应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'sample',
    'sample01',
]
# 需要加载的插件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 根URL解析文件
ROOT_URLCONF = 'chapter19.urls'
# 模板
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
            ],
        },
    },
]
# 配置WSGI服务路径
WSGI_APPLICATION = 'chapter19.wsgi.application'

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 密码配置选项
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

# 国际化配置

LANGUAGE_CODE = 'zh_Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

USE_THOUSAND_SEPARATOR = True
NUMBER_GROUPING = 3

# 访问静态文件的url前缀
STATIC_URL = '/static/'
# 设置静态文件的搜索路径
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "sample/static"),
    os.path.join(BASE_DIR, "sample01/static"),
)
# 下面的配置是为部署时收集静态页面用的。
# 当运行 python manage.py collectstatic 的时候，
# 将所有STATICFILES_DIRS中的文件及文件夹以及各app中static中的文件，
# 都复制到collected_static目录，以方便部署。
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
# uwsgi --http :8000 --wsgi-file chapter19/wsgi.py --static-map=/static=./collected_static

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
    },
}
"""