#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: file.py
@time: 2017/3/30 下午5:53
"""


import json
import logging
from datetime import datetime

from flask import request, render_template, redirect, url_for, g, abort, flash, jsonify
from flask import send_from_directory
from flask_login import current_user, login_required

from app_frontend import app

from flask import Blueprint


bp_file = Blueprint('file', __name__, url_prefix='/file')


log = logging.getLogger(__name__)


def allowed_file(filename):
    """
    校验文件类型
    """
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def get_extend_type(filename):
    """
    获取文件扩展
    :param filename:
    :return:
    """
    if allowed_file(filename):
        return filename.rsplit('.', 1)[1]
    else:
        return


def get_file_size(file_obj):
    """
    获取文件大小
    :param file_obj:
    :return:
    """
    file_obj.seek(0, 2)  # Seek to the end of the file
    size = file_obj.tell()  # Get the position of EOF
    file_obj.seek(0)  # Reset the file position to the beginning
    return size


@bp_file.route('/uploads', methods=['GET', 'POST'])
def uploads():
    """
    多文件上传
    """
    if request.method == 'GET':
        return render_template('uploads.html')
    if request.method == 'DELETE':
        # todo
        result = {"files": [
            {
                "picture1.jpg": True
            },
            {
                "picture2.jpg": True
            }
        ]}
        return json.dumps(result)
    if request.method == 'POST':
        files = []
        from werkzeug.utils import secure_filename
        file_list = request.files.getlist('files[]')
        for file_item in file_list:
            # file_name = secure_filename(file_item.filename)
            extend_type = get_extend_type(file_item.filename)
            file_name = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
            file_name = '%s.%s' % (file_name, extend_type) if extend_type else file_item.filename
            file_info = {
                'name': file_name,
                'content_type': file_item.content_type,
                'size': get_file_size(file_item),
                'url': url_for('static', filename='uploads/%s' % file_name),
                'thumbnail_url': url_for('static', filename='uploads/%s' % file_name),
                'delete_url': url_for('file.delete'),
                'delete_type': 'POST'
            }
            if not extend_type:
                file_info['thumbnail_url'] = url_for('static', filename='img/lazy-pic.png')
                file_info.pop('url')
                file_info.pop('delete_url')
            if not file_item or not allowed_file(file_item.filename):
                file_info['error'] = u'文件类型暂不支持'
            file_item.save(app.config['UPLOAD_FOLDER'] + file_info['name'])
            files.append(file_info)
        return json.dumps({'files': files})


@bp_file.route('/preview/<filename>', methods=['GET'])
def preview(filename):
    """
    预览图
    :return:
    """
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename=filename)


@bp_file.route('/thumbnail/<filename>', methods=['GET'])
def thumbnail(filename):
    """
    缩略图
    :return:
    """
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename=filename)


@bp_file.route('/del', methods=['GET', 'POST'])
def delete():
    """
    删除文件
    """
    if request.method == 'POST':
        # todo
        result = {"files": [
            {
                "picture1.jpg": True
            },
            {
                "picture2.jpg": True
            }
        ]}
        return json.dumps(result)
