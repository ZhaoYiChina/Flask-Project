#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2017/8/1 下午2:59
"""


import os
from importlib import import_module


MODE = os.environ.get('MODE') or 'default'


try:
    current_config = import_module('config.' + MODE)
except ImportError:
    print u'[!] 配置错误，请初始化环境变量'
    print u'source env_develop.sh  # 开发环境'
    print u'source env_product.sh  # 生产环境'
