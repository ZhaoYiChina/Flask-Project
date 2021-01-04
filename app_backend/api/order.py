#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: order.py
@time: 2017/4/13 下午9:45
"""


from datetime import datetime
from sqlalchemy import func

from app_backend.models import Order, ApplyGet, ApplyPut
from app_backend.tools.db import get_row, get_lists, get_rows, get_row_by_id, add, edit, delete
from app_backend.database import db
from app_common.maps.status_audit import STATUS_AUDIT_SUCCESS
from app_common.maps.status_order import STATUS_ORDER_COMPLETED, STATUS_ORDER_PROCESSING
from app_common.tools.date_time import get_hours, get_current_day_time_ends, time_local_to_utc, \
    get_current_month_time_ends, get_days, get_current_year_time_ends, get_months


def get_order_row_by_id(order_id):
    """
    通过 id 获取订单信息
    :param order_id:
    :return: None/object
    """
    return get_row_by_id(Order, order_id)


def get_order_row(*args, **kwargs):
    """
    获取订单信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(Order, *args, **kwargs)


def add_order(order_data):
    """
    添加订单信息
    :param order_data:
    :return: None/Value of order.id
    """
    return add(Order, order_data)


def edit_order(order_id, order_data):
    """
    修改订单信息
    :param order_id:
    :param order_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(Order, order_id, order_data)


def delete_order(order_id):
    """
    删除订单信息
    :param order_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(Order, order_id)


def get_order_lists(*args, **kwargs):
    """
    获取订单列表
    :param args:
    :param kwargs:
    :return: None/list
    """
    return get_lists(Order, *args, **kwargs)


def get_order_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取订单列表（分页）
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
    rows = get_rows(Order, page, per_page, *args, **kwargs)
    return rows


def get_put_match_order_rows(apply_put_id):
    """
    获取投资匹配订单列表
    :param apply_put_id:
    :return: list
    """
    try:
        rows = db.session.query(Order, ApplyGet). \
            filter(Order.apply_put_id == apply_put_id, ApplyGet.id == Order.apply_get_id). \
            all()
        db.session.commit()
        return rows
    except Exception as e:
        db.session.rollback()
        raise e


def get_get_match_order_rows(apply_get_id):
    """
    获取提现匹配订单列表
    :param apply_get_id:
    :return: list
    """
    try:
        rows = db.session.query(Order, ApplyPut). \
            filter(Order.apply_get_id == apply_get_id, ApplyPut.id == Order.apply_put_id). \
            all()
        db.session.commit()
        return rows
    except Exception as e:
        db.session.rollback()
        raise e


def flow(order_id, next_uid):
    """
    订单流转
    :param order_id:
    :param next_uid:
    :return:
    """
    # 获取订单信息
    # 新增投资
    # 新增匹配订单（流转类型）
    # 修改原始订单（流转状态）
    # 新增订单流转记录


def order_stats(time_based='hour'):
    """
    订单金额统计
    :return:
    """
    # 按小时统计
    if time_based == 'hour':
        start_time, end_time = get_current_day_time_ends()
        hours = get_hours(False)
        hours_zerofill = get_hours()
        result = dict(zip(hours, [0] * len(hours)))
        rows = db.session \
            .query(func.hour(Order.create_time).label('hour'), func.sum(Order.money)) \
            .filter(Order.create_time >= time_local_to_utc(start_time),
                    Order.create_time <= time_local_to_utc(end_time)) \
            .group_by('hour') \
            .limit(len(hours)) \
            .all()
        result.update(dict(rows))
        return [(hours_zerofill[i], result[hour]) for i, hour in enumerate(hours)]
    # 按日期统计
    if time_based == 'date':
        start_time, end_time = get_current_month_time_ends()
        today = datetime.today()
        days = get_days(year=today.year, month=today.month, zerofill=False)
        days_zerofill = get_days(year=today.year, month=today.month)
        result = dict(zip(days, [0] * len(days)))
        rows = db.session \
            .query(func.day(Order.create_time).label('date'), func.sum(Order.money)) \
            .filter(Order.create_time >= time_local_to_utc(start_time),
                    Order.create_time <= time_local_to_utc(end_time)) \
            .group_by('date') \
            .limit(len(days)) \
            .all()
        result.update(dict(rows))
        return [(days_zerofill[i], result[day]) for i, day in enumerate(days)]
    # 按月份统计
    if time_based == 'month':
        start_time, end_time = get_current_year_time_ends()
        months = get_months(False)
        months_zerofill = get_months()
        result = dict(zip(months, [0] * len(months)))
        rows = db.session \
            .query(func.month(Order.create_time).label('month'), func.sum(Order.money)) \
            .filter(Order.create_time >= time_local_to_utc(start_time),
                    Order.create_time <= time_local_to_utc(end_time)) \
            .group_by('month') \
            .limit(len(months)) \
            .all()
        result.update(dict(rows))
        return [(months_zerofill[i], result[month]) for i, month in enumerate(months)]
