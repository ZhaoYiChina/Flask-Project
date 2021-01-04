#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: auth.py
@time: 2017/3/10 下午11:44
"""

import json
from datetime import datetime

from flask import Blueprint
from flask import g, request, render_template, jsonify
from flask import session, redirect, url_for, flash
from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from itsdangerous import TimestampSigner, SignatureExpired, BadTimeSignature

from app_common.maps import area_code_map
from app_common.maps.type_auth import *
from app_common.tools import md5
from app_common.tools.ip import get_real_ip
from app_frontend import app, oauth_github, oauth_qq, oauth_weibo
from app_frontend.api.user import edit_user
from app_frontend.api.user import get_user_row_by_id
from app_frontend.api.user_auth import get_user_auth_row
from app_frontend.forms.login import LoginPhoneForm
from app_frontend.forms.login import LoginForm


SWITCH_LOGIN_ACCOUNT = app.config['SWITCH_LOGIN_ACCOUNT']
SWITCH_LOGIN_PHONE = app.config['SWITCH_LOGIN_PHONE']
SWITCH_LOGIN_EMAIL = app.config['SWITCH_LOGIN_EMAIL']

SWITCH_LOGIN_THREE_PART = app.config['SWITCH_LOGIN_THREE_PART']

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


@bp_auth.route('/index/', methods=['GET', 'POST'])
def index():
    """
    账号登录认证
    """
    if current_user and current_user.is_authenticated:
        return redirect(url_for('index'))
    if not SWITCH_LOGIN_ACCOUNT:
        flash(u'账号登录功能关闭，暂不支持账号登录', 'warning')
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # 获取认证信息
            condition = {
                'type_auth': TYPE_AUTH_ACCOUNT,
                'auth_key': form.account.data,
                'auth_secret': md5(form.password.data)
            }
            user_auth_info = get_user_auth_row(**condition)
            if user_auth_info is None:
                flash(u'%s, 登录失败，请检查内容后重新登录' % form.account.data, 'warning')
                return render_template('auth/index.html', title='login', form=form)
            if user_auth_info.status_verified == 0:
                flash(u'%s, 登录账号尚未验证，请先验证账号' % form.account.data, 'warning')
                return render_template('auth/index.html', title='login', form=form)
            # session['logged_in'] = True

            # 用 login_user 函数来登入他们
            login_user(get_user_row_by_id(user_auth_info.user_id), remember=form.remember.data)
            flash(u'%s, 恭喜，您已成功登录' % form.account.data, 'success')
            return redirect(request.args.get('next') or url_for('index'))
        # flash(form.errors, 'warning')  # 调试打开
    return render_template('auth/index.html', title='login', form=form, SWITCH_LOGIN_THREE_PART=SWITCH_LOGIN_THREE_PART)


@bp_auth.route('/phone/', methods=['GET', 'POST'])
def phone():
    """
    手机登录认证
    """
    if current_user and current_user.is_authenticated:
        return redirect(url_for('index'))
    if not SWITCH_LOGIN_PHONE:
        flash(u'手机登录功能关闭，暂不支持手机登录', 'warning')
        return redirect(url_for('index'))
    form = LoginPhoneForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # 手机号码国际化
            area_id = form.area_id.data
            area_code = area_code_map.get(area_id, '86')
            mobile_iso = '%s%s' % (area_code, form.phone.data)
            # 获取认证信息
            condition = {
                'type_auth': TYPE_AUTH_PHONE,
                'auth_key': mobile_iso,
                'auth_secret': md5(form.password.data)
            }
            user_auth_info = get_user_auth_row(**condition)
            if not user_auth_info:
                flash(u'%s, 登录失败，请检查内容后重新登录' % form.phone.data, 'warning')
                return render_template('auth/phone.html', title='login', form=form)
            if user_auth_info.status_verified == 0:
                flash(u'%s, 登录手机尚未验证，请先验证手机' % form.phone.data, 'warning')
                return render_template('auth/phone.html', title='login', form=form)
            # session['logged_in'] = True

            # 用 login_user 函数来登入他们
            login_user(get_user_row_by_id(user_auth_info.user_id), remember=form.remember.data)
            flash(u'%s, 恭喜，您已成功登录' % form.phone.data, 'success')
            return redirect(request.args.get('next') or url_for('index'))
        # flash(form.errors, 'warning')  # 调试打开
    return render_template('auth/phone.html', title='login', form=form, SWITCH_LOGIN_THREE_PART=SWITCH_LOGIN_THREE_PART)


@bp_auth.route('/email/', methods=['GET', 'POST'])
def email():
    """
    邮箱登录认证
    """
    if current_user and current_user.is_authenticated:
        return redirect(url_for('index'))
    if not SWITCH_LOGIN_EMAIL:
        flash(u'邮箱登录功能关闭，暂不支持邮箱登录', 'warning')
        return redirect(url_for('index'))
    from app_frontend.forms.login import LoginEmailForm
    form = LoginEmailForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # 获取认证信息
            condition = {
                'type_auth': TYPE_AUTH_EMAIL,
                'auth_key': form.email.data,
                'auth_secret': md5(form.password.data)
            }
            user_auth_info = get_user_auth_row(**condition)
            if user_auth_info is None:
                flash(u'%s, 登录失败，请检查内容后重新登录' % form.email.data, 'warning')
                return render_template('auth/email.html', title='login', form=form)
            if user_auth_info.status_verified == 0:
                flash(u'%s, 登录邮箱尚未验证，请先验证邮箱' % form.email.data, 'warning')
                return render_template('auth/email.html', title='login', form=form)
            # session['logged_in'] = True

            # 用 login_user 函数来登入他们
            login_user(get_user_row_by_id(user_auth_info.user_id), remember=form.remember.data)
            flash(u'%s, 恭喜，您已成功登录' % form.email.data, 'success')
            return redirect(request.args.get('next') or url_for('index'))
        # flash(form.errors, 'warning')  # 调试打开
    return render_template('auth/email.html', title='login', form=form, SWITCH_LOGIN_THREE_PART=SWITCH_LOGIN_THREE_PART)


# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash(u'You were logged out')
#     return redirect(url_for('index'))


@bp_auth.route('/logout/')
def logout():
    """
    退出登录
    """
    logout_user()
    session.pop('qq_token', None)
    session.pop('weibo_token', None)
    session.pop('github_token', None)
    flash(u'您已成功退出登录', 'info')
    return redirect(url_for('index'))


# # 第三方登录（QQ）
def json_to_dict(x):
    """
    OAuthResponse class can't not parse the JSON data with content-type
    text/html, so we need reload the JSON data manually
    :param x:
    :return:
    """
    if x.find('callback') > -1:
        pos_lb = x.find('{')
        pos_rb = x.find('}')
        x = x[pos_lb:pos_rb + 1]
    try:
        return json.loads(x, encoding='utf-8')
    except:
        return x


def update_qq_api_request_data(data={}):
    """
    Update some required parameters for OAuth2.0 API calls
    :param data:
    :return:
    """
    defaults = {
        'openid': session.get('qq_openid'),
        'access_token': session.get('qq_token')[0],
        'oauth_consumer_key': app.config['consumer_key'],
    }
    defaults.update(data)
    return defaults


@bp_auth.route('/user_info')
def get_user_info():
    if 'qq_token' in session:
        data = update_qq_api_request_data()
        resp = oauth_qq.get('/user/get_user_info', data=data)
        return jsonify(status=resp.status, data=resp.data)
    return redirect(url_for('login_qq'))


@bp_auth.route('/login/qq/')
def login_qq():
    return oauth_qq.authorize(callback=url_for('auth.authorized_qq', _external=True))


@bp_auth.route('/login/authorized/qq/')
def authorized_qq():
    resp = oauth_qq.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['qq_token'] = (resp['access_token'], '')

    # Get openid via access_token, openid and access_token are needed for API calls
    resp = oauth_qq.get('/oauth2.0/me', {'access_token': session['qq_token'][0]})
    resp = json_to_dict(resp.data)
    if isinstance(resp, dict):
        session['qq_openid'] = resp.get('openid')

    return redirect(url_for('get_user_info'))


@oauth_qq.tokengetter
def get_qq_oauth_token():
    return session.get('qq_token')


# 第三方登录（WeiBo）
# @app.route('/')
# def index():
#     if 'oauth_token' in session:
#         access_token = session['oauth_token'][0]
#         resp = weibo.get('statuses/home_timeline.json')
#         return jsonify(resp.data)
#     return redirect(url_for('auth.index'))


@bp_auth.route('/login/weibo/')
def login_weibo():
    return oauth_weibo.authorize(callback=url_for('auth.authorized_weibo',
                                                  next=request.args.get('next') or request.referrer or None,
                                                  _external=True))


@bp_auth.route('/login/authorized/weibo/')
def authorized_weibo():
    resp = oauth_weibo.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    return redirect(url_for('index'))


@oauth_weibo.tokengetter
def get_weibo_oauth_token():
    return session.get('oauth_token')


def change_weibo_header(uri, headers, body):
    """Since weibo is a rubbish server, it does not follow the standard,
    we need to change the authorization header for it."""
    auth = headers.get('Authorization')
    if auth:
        auth = auth.replace('Bearer', 'OAuth2')
        headers['Authorization'] = auth
    return uri, headers, body


oauth_weibo.pre_request = change_weibo_header


# 第三方登录（GitHub）
@bp_auth.route('/login/github/')
def login_github():
    return oauth_github.authorize(callback=url_for('auth.authorized_github', _external=True))


@bp_auth.route('/login/authorized/github/')
def authorized_github():
    resp = oauth_github.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error'],
            request.args['error_description']
        )
    session['github_token'] = (resp['access_token'], '')
    me = oauth_github.get('user')
    return jsonify(me.data)


@oauth_github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')


@bp_auth.route('/admin_login/', methods=['GET', 'POST'])
def admin_login():
    """
    管理后台登录前台账号认证
    """
    # 获取签名的uid
    uid_sign = request.args.get('uid_sign', '', type=str)

    time_out = app.config.get('ADMIN_TO_USER_LOGIN_TIME_OUT')
    sign_key = app.config.get('ADMIN_TO_USER_LOGIN_SIGN_KEY')
    s = TimestampSigner(sign_key)
    try:
        # 签名解密
        uid = s.unsign(uid_sign, max_age=time_out)
    except SignatureExpired as e:
        # 处理签名超时
        # raise Exception(e.message)
        flash(u'登录超时：%s' % e.message, 'warning')
        return redirect(request.args.get('next') or url_for('index'))
    except BadTimeSignature as e:
        # 处理签名错误
        # raise Exception(e.message)
        flash(u'登录错误：%s' % e.message, 'warning')
        return redirect(request.args.get('next') or url_for('index'))

    # 获取认证信息
    condition = {
        'type_auth': TYPE_AUTH_ACCOUNT,
        'user_id': uid
    }
    user_auth_info = get_user_auth_row(**condition)
    if user_auth_info is None:
        flash(u'登录失败，请检查内容后重新登录', 'warning')
        return redirect(request.args.get('next') or url_for('index'))
    if user_auth_info.status_verified == 0:
        flash(u'%s, 登录账号尚未验证，请先验证账号' % user_auth_info.auth_key, 'warning')
        return redirect(request.args.get('next') or url_for('index'))

    login_user(get_user_row_by_id(uid))
    flash(u'%s, 恭喜，您已成功登录' % user_auth_info.auth_key, 'success')
    return redirect(request.args.get('next') or url_for('index'))
