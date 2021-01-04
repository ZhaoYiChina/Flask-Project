#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: apply_put.py
@time: 2017/4/13 下午9:45
"""


from app_common.tools.date_time import get_current_day_time_ends, get_current_month_time_ends
from app_frontend.models import ApplyPut
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete, count
from app_common.maps.status_delete import *
from app_frontend.database import db
from sqlalchemy.sql import func
from app_common.maps.status_order import *
from app_common.maps.status_delete import *


def get_apply_put_row_by_id(apply_put_id):
    """
    通过 id 获取投资申请信息
    :param apply_put_id:
    :return: None/object
    """
    return get_row_by_id(ApplyPut, apply_put_id)


def get_apply_put_row(*args, **kwargs):
    """
    获取投资申请信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(ApplyPut, *args, **kwargs)


def add_apply_put(apply_put_data):
    """
    添加投资申请信息
    :param apply_put_data:
    :return: None/Value of apply_put.id
    """
    return add(ApplyPut, apply_put_data)


def edit_apply_put(apply_put_id, apply_put_data):
    """
    修改投资申请信息
    :param apply_put_id:
    :param apply_put_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(ApplyPut, apply_put_id, apply_put_data)


def delete_apply_put(apply_put_id):
    """
    删除投资申请信息
    :param apply_put_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(ApplyPut, apply_put_id)


def get_apply_put_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取投资申请列表（分页）
    Usage:
        items: 信息列表
        has_next: 如果本页之后还有超过一个分页，则返回True
        has_prev: 如果本页之前还有超过一个分页，则返回True
        next_num: 返回下一页的页码
        prev_num: 返回上一页的页码
        iter_pages(): 页码列表
        iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2) 页码列表默认参数
    :param page:
    :param per_page:
    :param args:
    :param kwargs:
    :return:
    """
    rows = get_rows(ApplyPut, page, per_page, *args, **kwargs)
    return rows


def is_put(user_id):
    """
    是否投资
    :param user_id:
    :return:
    """
    condition = {
        'user_id': user_id,
        'status_delete': STATUS_DEL_NO
    }
    return bool(count(ApplyPut, **condition))


def get_current_day_put_amount(user_id=None):
    """
    获取当天投资总额
    :return:
    """
    start_time, end_time = get_current_day_time_ends()
    condition = [
        ApplyPut.create_time >= start_time,
        ApplyPut.create_time <= end_time
    ]
    if user_id:
        condition.append(ApplyPut.user_id == user_id)
    res = db.session \
        .query(func.sum(ApplyPut.money_apply).label('amount')) \
        .filter(*condition) \
        .first()
    return res.amount or 0


def get_current_month_put_amount(user_id=None):
    """
    获取当月投资总额
    :return:
    """
    start_time, end_time = get_current_month_time_ends()
    condition = [
        ApplyPut.create_time >= start_time,
        ApplyPut.create_time <= end_time
    ]
    if user_id:
        condition.append(ApplyPut.user_id == user_id)
    res = db.session \
        .query(func.sum(ApplyPut.money_apply).label('amount')) \
        .filter(*condition) \
        .first()
    return res.amount or 0


def get_put_processing_amount(user_id):
    """
    获取用户投资申请未匹配总金额
    :param user_id:
    :return:
    """
    condition = [
        ApplyPut.user_id == user_id,
        ApplyPut.status_order <= int(STATUS_ORDER_COMPLETED),
        ApplyPut.status_delete == int(STATUS_DEL_NO)
    ]
    res = db.session \
        .query(func.sum(ApplyPut.money_apply).label('money_apply_amount'),
               func.sum(ApplyPut.money_order).label('money_order_amount')) \
        .filter(*condition) \
        .first()
    return (res.money_apply_amount or 0) - (res.money_order_amount or 0)


def get_put_processing_count(user_id):
    """
    获取用户投资申请未匹配总单数
    :param user_id:
    :return:
    """
    condition = [
        ApplyPut.user_id == user_id,
        ApplyPut.status_order <= int(STATUS_ORDER_COMPLETED),
        ApplyPut.status_delete == int(STATUS_DEL_NO)
    ]
    num = count(ApplyPut, *condition)
    return num
