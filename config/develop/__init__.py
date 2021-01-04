#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2017/5/19 下午11:25
"""


import os
import socket
from datetime import timedelta

# 网站运营配置
from settings import *
from settings.apply import *
from settings.interest import *
from settings.order import *
from settings.sms import *
from settings.user import *

# 测试模式开关
TEST = True

# 前端地址
FRONTEND_URL = 'http://0.0.0.0:8000'

DEBUG = True

PROJECT_NAME = u'网站名称'

ICP_CODE = u'沪ICP备12024750号'

BASE_DIR = os.path.abspath(os.path.dirname(__file__)+'/../../')

# 获取服务器名称
HOST_NAME = socket.getfqdn(socket.gethostname())
# 获取服务器内网ip
# HOST_IP = socket.gethostbyname(HOST_NAME)

HOST_IP = '192.168.4.1'

# requests 超时设置
REQUESTS_TIME_OUT = (30, 30)


# 数据库 MySQL
DB_MYSQL = {
    'host': HOST_IP,
    'user': 'root',
    'passwd': '123456',
    'port': 3306,
    'db': 'flask_project',
    'charset': 'utf8'
}

SQLALCHEMY_DATABASE_URI_MYSQL = \
    'mysql+mysqldb://%s:%s@%s:%s/%s?charset=%s' % \
    (DB_MYSQL['user'], DB_MYSQL['passwd'], DB_MYSQL['host'], DB_MYSQL['port'], DB_MYSQL['db'], DB_MYSQL['charset'])

# 数据库 PostgreSQL
DB_PG = {
    'host': HOST_IP,
    'user': 'postgres',
    'password': 'postgres',  # 可修改 \password
    'port': 5432,
    'database': 'test'
}

SQLALCHEMY_DATABASE_URI_PG = \
    'postgresql://%s:%s@%s:%s/%s' % \
    (DB_PG['user'], DB_PG['password'], DB_PG['host'], DB_PG['port'], DB_PG['database'])

# 数据库 SQLite
DB_SQLITE = os.path.join(BASE_DIR, 'db/data/flask.db')

SQLALCHEMY_DATABASE_URI_SQLITE = 'sqlite:///' + DB_SQLITE


SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI_MYSQL
# SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 打开自动提交 官方已经移除(http://flask-sqlalchemy.pocoo.org/2.1/changelog/#version-2-0)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 5  # 默认 pool_size=5
SQLALCHEMY_POOL_TIMEOUT = 10  # 默认 10秒
SQLALCHEMY_POOL_RECYCLE = 500  # 配置要小于 数据库配置 wait_timeout
SQLALCHEMY_ECHO = True


REDIS = {
    'host': HOST_IP,
    'port': 6379,
    'db': 0,
    'password': None
}

DB_MONGO = {
    'host': HOST_IP,
    'port': 27017,
    'username': '',
    'password': '',
    'database': ''
}

RABBIT_MQ = {
    'host': HOST_IP,
    'port': 5672
}

EXCHANGE_NAME = 'amq.direct'

# 验证码类型
CAPTCHA_ENTITY = [
    'reg',      # 注册
    'login',    # 登录
    'reset'     # 重置密码（找回密码）
]


# 短信签名（简称）
SMS_SIGNER = u'网站签名'
# 短信接口配置
SMS = {
    'UN': 'I6814767',           # 创蓝账号
    'PW': 'UDqQ1dcvTg2052',     # 创蓝密码
}

# 隧道配置
SSH_CONFIG = {
    'IP': '120.76.40.92',
    'PORT': 22,
    'USERNAME': 'root',
    'PASSWORD': 't3#R@r6FrTHK',
    'DB_MYSQL': {
        'host': '127.0.0.1',
        'user': 'root',
        'passwd': '..++**//520..',
        'port': 3306,
        'db': 'mm7w'
    }
}


CSRF_ENABLED = True
SECRET_KEY = '\x03\xabjR\xbbg\x82\x0b{\x96f\xca\xa8\xbdM\xb0x\xdbK%\xf2\x07\r\x8c'

# 会话配置
# PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)             # 登录状态保持，默认31天
REMEMBER_COOKIE_DURATION = timedelta(days=14)   # 记住登录状态，默认365天
LOGIN_MESSAGE = u'请登录后操作'
LOGIN_MESSAGE_CATEGORY = 'warning'  # 默认'message'


# 后台登录前台配置
ADMIN_TO_USER_LOGIN_TIME_OUT = 1200
ADMIN_TO_USER_LOGIN_SIGN_KEY = '1b106105da7e88e54d42e3f4356e41d8'

# 用户推广链接配置
USER_INVITE_LINK_SIGN_KEY = 'ff99bae31b7bd480deee291dd55d6864'

# 文件上传配置
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app_frontend/static/uploads/')
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_CONTENT_LENGTH = 2.6 * 1024 * 1024  # 2.6Mb
MIN_CONTENT_LENGTH = 2.0 * 1024         # 2.0Kb

# Celery 配置 （异步任务队列/基于分布式消息传递的作业队列）
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
# CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'amqp://guest:guest@localhost:5672//'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# 本地调试邮箱配置
# $ sudo python -m smtpd -n -c DebuggingServer localhost:25
MAIL_SERVER = 'localhost',
MAIL_PORT = 25,
MAIL_USERNAME = None,
MAIL_PASSWORD = None,
MAIL_DEFAULT_SENDER = ('no-reply', 'no-reply@localhost')
# 后台管理人员邮件列表
ADMINS = ['455091702@qq.com']

# 开发环境邮箱配置
# MAIL_SERVER = 'smtp.163.com',
# MAIL_PORT = 25,
# MAIL_USERNAME = 'xxxxxx@163.com',
# MAIL_PASSWORD = 'xxxxxx',
# MAIL_DEFAULT_SENDER = (u'系统邮箱', 'zhang_he06@163.com')
# # 后台管理人员邮件列表
# ADMINS = ['455091702@qq.com']


# sendcloud 邮件发送平台
SENDCLOUD_API_USER = 'zhang_he_test_w6kIMK'
SENDCLOUD_API_KEY = 'eZeC3Qwciv4o0lDH'

# qiniu 云存储
QINIU_ACCESS_KEY = 'i3Zi_VQOoeuMDnYkksWvn6TKa0_2C9Wb2NXMtrdn'
QINIU_SECRET_KEY = 'B_0pOtxxaQX8aPqqdMqX2A5v0R99KYKgod5vbkXf'
QINIU_BUCKET_NAME = 'zhendi-open'                       # 七牛空间名称
QINIU_BUCKET_DOMAIN = '7xtmj9.com2.z0.glb.clouddn.com'  # 七牛空间对应域名

# 第三方开放授权登陆

GITHUB_OAUTH = {
    'consumer_key': '0ccd9367a1f81288b127',
    'consumer_secret': '711b6afcc938d760e9e57215dfbdcb115150ddc6',
    'request_token_params': {'scope': 'user:email'},
    'base_url': 'https://api.github.com/',
    'request_token_url': None,
    'access_token_method': 'POST',
    'access_token_url': 'https://github.com/login/oauth/access_token',
    'authorize_url': 'https://github.com/login/oauth/authorize'
}

QQ_OAUTH = {
    'consumer_key': '101187283',  # QQ_APP_ID
    'consumer_secret': '993983549da49e384d03adfead8b2489',  # QQ_APP_KEY
    'base_url': 'https://graph.qq.com',
    'request_token_url': None,
    'request_token_params': {'scope': 'get_user_info'},
    'access_token_url': '/oauth2.0/token',
    'authorize_url': '/oauth2.0/authorize',
}

WEIBO_OAUTH = {
    'consumer_key': '909122383',
    'consumer_secret': '2cdc60e5e9e14398c1cbdf309f2ebd3a',
    'request_token_params': {'scope': 'email,statuses_to_me_read'},
    'base_url': 'https://api.weibo.com/2/',
    'authorize_url': 'https://api.weibo.com/oauth2/authorize',
    'request_token_url': None,
    'access_token_method': 'POST',
    'access_token_url': 'https://api.weibo.com/oauth2/access_token',
    # since weibo's response is a shit, we need to force parse the content
    'content_type': 'application/json',
}


# 日志参数配置
LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'detail': {
            'format': '%(asctime)s - %(name)s - File: %(filename)s - line: %(lineno)d - %(funcName)s() - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'INFO'
        },
        'file_app': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'detail',
            'level': 'DEBUG',
            'when': 'D',
            'filename': BASE_DIR + '/logs/app.log'
        },
        'file_db': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'detail',
            'level': 'DEBUG',
            'when': 'D',
            'filename': BASE_DIR + '/logs/db.log'
        }
    },
    'loggers': {
        'app': {
            'handlers': ['console', 'file_app'],
            'level': 'DEBUG'
        },
        'db': {
            'handlers': ['file_db'],
            'level': 'DEBUG'
        }
    }
}


if __name__ == '__main__':
    import os
    import binascii

    sk = os.urandom(16)
    print sk
    print binascii.b2a_hex(sk)
    print BASE_DIR
    print UPLOAD_FOLDER
    print SQLALCHEMY_DATABASE_URI
    print HOST_IP
