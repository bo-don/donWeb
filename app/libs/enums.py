# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         : don
@Software       : PyCharm
------------------------------------
@File           :  enums.py
@Description    :  自定义枚举
@CreateTime     :  2024/03/11
------------------------------------
"""

from enum import Enum


class EnumCode(Enum):
    """
    自定义错误码
    """

    @property
    def code(self):
        """
        获取错误码
        """
        return self.value[0]

    @property
    def msg(self):
        """
        获取错误码信息
        """
        return self.value[1]


class BusinessCodeEnums(EnumCode):
    # BaseCode
    BaseCode = ('500', 'Service Error')

    # 无权限
    ForbiddenError = ('403', 'Forbidden')
