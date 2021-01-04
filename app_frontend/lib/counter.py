#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: count.py
@time: 16-1-27 下午3:03
"""


import redis
from copy import deepcopy


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
redis_pipeline = redis_client.pipeline()


class Counter(object):
    """
    计数器
    """
    # 定义支持的实体类型
    entity_name_list = ['user', 'blog', 'topic', 'subject', 'product']

    # 定义支持的统计类型
    stat_type_list = [
        'favor',  # 支持
        'decry',  # 反对
        'follow',  # 关注
        'fans',  # 粉丝
        'view',  # 点击
        'collect',  # 收藏
        'flag'  # 举报
    ]

    # 定义用户计数器结构
    user_counter_dict = {
        'favor': '0',  # 支持数
        'decry': '0',  # 反对数
        'follow': '0',  # 关注数
        'fans': '0'  # 粉丝数
    }

    # 定义话题计数器结构
    topic_counter_dict = {
        'favor': '0',  # 支持数
        'decry': '0',  # 反对数
        'view': '0',  # 点击数
        'collect': '0'  # 收藏数
    }

    # 定义博客计数器结构
    blog_counter_dict = {
        'favor': '0',  # 支持数
        'flag': '0',  # 举报数
        'view': '0',  # 点击数
        'collect': '0'  # 收藏数
    }

    def __init__(self, entity_name, prefix='counter'):
        if entity_name not in self.entity_name_list:
            raise TypeError(u'类型错误')
        self.entity_name = entity_name
        self.prefix = prefix

    def increase(self, item_id, stat_type, num=1):
        """
        增加次数
        :param item_id:
        :param stat_type:
        :param num:
        :return:
        """
        if stat_type not in self.stat_type_list:
            raise TypeError(u'类型错误')
        key = "%s:%s:%s" % (self.prefix, self.entity_name, item_id)
        # 判断物品是否存在
        if redis_client.exists(key):
            redis_client.hincrby(key, stat_type, num)
        else:
            # 如果不存在，添加物品至购物车
            redis_client.hmset(key, {stat_type: num})
        return True

    def decrease(self, item_id, stat_type, num=1):
        """
        减少次数
        :param item_id:
        :param stat_type:
        :param num:
        :return:
        """
        key = "%s:%s:%s" % (self.prefix, self.entity_name, item_id)
        # 判断物品是否存在
        if redis_client.exists(key):
            if num >= int(redis_client.hget(key, stat_type)):
                # 如果超过，设置默认最小数量
                redis_client.hmset(key, {stat_type: 1})
            else:
                redis_client.hincrby(key, stat_type, -num)
        return True

    def del_item(self, item_id):
        """
        删除物品
        :param item_id:
        :return:
        """
        key = "%s:%s:%s" % (self.prefix, self.entity_name, item_id)
        # 判断物品是否存在
        if redis_client.exists(key):
            redis_client.delete(key)
        return True

    def counter_blog_item(self, blog_id):
        """
        显示 blog 计数器
        :param blog_id:
        :return:
        """
        key = "%s:%s:%s" % (self.prefix, self.entity_name, blog_id)
        # 判断物品是否存在
        blog_dict = deepcopy(self.blog_counter_dict)
        if redis_client.exists(key):
            redis_result = redis_client.hgetall(key)
            blog_dict.update(redis_result)
        return blog_dict

    def counter_user_list_all(self):
        """
        显示全部用户计数器
        :return:
        """
        key = "%s:%s:*" % (self.prefix, self.entity_name)
        cnt_key_list = redis_client.keys(key)
        cnt_list = []
        for item in cnt_key_list:
            user_dict = deepcopy(self.user_counter_dict)  # 注意是深度复制，不能写成 user_dict = self.user_counter_dict
            user_dict.update(redis_client.hgetall(item))
            cnt_list.append(user_dict)
        return cnt_list

    def counter_user_list(self, uid_list):
        """
        显示用户计数器
        按原 uid_list 列表顺序返回结果
        :param uid_list:
        :return:
        """
        cnt_list = []
        for uid in uid_list:
            key = "%s:%s:%s" % (self.prefix, self.entity_name, uid)
            if redis_client.exists(key):
                user_dict = deepcopy(self.user_counter_dict)
                redis_result = redis_client.hgetall(key)
                user_dict.update(redis_result)
                cnt_list.append(user_dict)
        return cnt_list

    def counter_topic_list(self, topic_list):
        """
        显示话题计数器
        按原 uid_list 列表顺序返回结果
        :param topic_list:
        :return:
        """
        cnt_list = []
        for topic in topic_list:
            key = "%s:%s:%s" % (self.prefix, self.entity_name, topic)
            user_dict = deepcopy(self.topic_counter_dict)
            if redis_client.exists(key):
                redis_result = redis_client.hgetall(key)
                user_dict.update(redis_result)
            cnt_list.append(user_dict)
        return cnt_list

    def counter_blog_list(self, blog_list):
        """
        显示 blog 计数器
        按原 blog_list 列表顺序返回结果
        :param blog_list:
        :return:
        """
        cnt_list = []
        for blog in blog_list:
            key = "%s:%s:%s" % (self.prefix, self.entity_name, blog)
            blog_dict = deepcopy(self.blog_counter_dict)
            if redis_client.exists(key):
                redis_result = redis_client.hgetall(key)
                blog_dict.update(redis_result)
            cnt_list.append(blog_dict)
        return cnt_list

    def set_blog_counter(self, blog_id, stat_type, num=1):
        """
        设置 blog 计数器
        :param blog_id:
        :param stat_type:
        :param num:
        :return:
        """
        self.increase(blog_id, stat_type, num)
        return self.counter_blog_item(blog_id)


def test_user():
    import json
    user_cnt_obj = Counter('user')
    user_cnt_obj.del_item(12)
    user_cnt_obj.del_item(13)
    user_cnt_obj.increase(12, 'favor')
    user_cnt_obj.increase(13, 'fans', 5)
    user_cnt_obj.increase(14, 'fans', 4)
    user_cnt_obj.increase(14, 'follow', 3)
    print json.dumps(user_cnt_obj.counter_user_list(['12', '13']), indent=4, ensure_ascii=False)
    print json.dumps(user_cnt_obj.counter_user_list_all(), indent=4, ensure_ascii=False)


def test_topic():
    import json
    topic_cnt_obj = Counter('topic')
    print json.dumps(topic_cnt_obj.counter_topic_list(['1', '2', '3']), indent=4, ensure_ascii=False)
    topic_cnt_obj.increase(4, 'fans', 4)
    print topic_cnt_obj.counter_blog_item(4)
    print topic_cnt_obj.set_blog_counter(4, 'flag')


if __name__ == '__main__':
    # test_user()
    test_topic()
