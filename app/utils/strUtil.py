# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         : don
@Software       : PyCharm
------------------------------------
@File           :  strUtil.py
@Description    :  字符串工具方法
@CreateTime     :  2024/03/11
------------------------------------
"""


class StrUtil(object):
    @classmethod
    def is_none(cls, param):
        """
        判断参数为空或空字符串
        :param param:
        :return:
        """
        if param == '' or param is None:
            return True
        else:
            return False

    @classmethod
    def is_not_none(cls, param):
        """
        判断参数不为空、空字符串
        :param param:
        :return:
        """
        if param != '' and param is not None:
            return True
        else:
            return False
