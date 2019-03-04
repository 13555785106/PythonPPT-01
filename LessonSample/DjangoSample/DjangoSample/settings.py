# -*- coding: utf-8 -*-

import os

# Django的默认全局配置文件是 django.conf.global_settings.py
# 可以通过 python manage.py diffsettings 显示当前设置文件与Django的默认设置之间的差异。

# 获取项目的根目录，即顶层的那个DjangoSample目录，不是当前settings.py所在的chapter19目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 秘钥串
SECRET_KEY = '1d3o7p)l-8h9cgm46s!f*0_s2bk3^c33&6n7jdy2h9ku#rtc*j'

# 是否开启调试。开发阶段必须开启，生产环境必须关闭。
DEBUG = True
# 允许访问的域名，生产环境必须设置
# ALLOWED_HOSTS = ['175.8.175.62','127.0.0.1']
ALLOWED_HOSTS = []
# 当前项目安装的应用

INSTALLED_APPS = [
    'ch01.apps.Ch01Config',
    'ch02.apps.Ch02Config',
    'ch03.apps.Ch03Config',
    'ch04.apps.Ch04Config',
    'ch05.apps.Ch05Config',
    'ch06.apps.Ch06Config',
    'django.contrib.admin',  # 管理框架
    'django.contrib.admindocs',
    'django.contrib.auth',  # 验证框架
    'django.contrib.contenttypes',  # app与表的关系框架
    'django.contrib.sessions',  # 会话框架
    'django.contrib.messages',  # 消息框架
    'django.contrib.staticfiles',  # 静态文件管理框架

]
# 需要加载的中间件或者说插件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
]
# 根URL解析文件
ROOT_URLCONF = 'DjangoSample.urls'
# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 指定查找网页模板的目录
        'APP_DIRS': True,  # 是否在相应的app下templates目录中查找网页模板
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
# WSGI应用入口
WSGI_APPLICATION = 'DjangoSample.wsgi.application'

# 数据库配置

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 密码校验配置选项

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
    os.path.join(BASE_DIR, "ch01/static"),
    os.path.join(BASE_DIR, "ch02/static"),
    os.path.join(BASE_DIR, "ch03/static"),
    os.path.join(BASE_DIR, "ch03/static"),
    os.path.join(BASE_DIR, "ch05/static"),
    os.path.join(BASE_DIR, "ch06/static"),
)
# 下面的配置是为部署时收集静态页面用的。
# 当运行 python manage.py collectstatic 的时候，
# 将所有STATICFILES_DIRS中的文件及文件夹以及各app中static中的文件，
# 都复制到collected_static目录，以方便部署。
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
# uwsgi --http :8000 --wsgi-file chapter19/wsgi.py --static-map=/static=./collected_static

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

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
