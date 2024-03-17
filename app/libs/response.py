# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         : don
@Software       : PyCharm
------------------------------------
@File           :  response.py
@Description    :  自定义响应
@CreateTime     :  2024/03/11
------------------------------------
"""
import traceback
from datetime import datetime
from typing import TypeVar, Generic, Optional, Any

from pydantic.generics import GenericModel

from app.libs.enums import BusinessCodeEnums
from app.libs.exceptions import BusinessError
from app.utils.encoder import jsonable_encoder

# 泛型类型
T = TypeVar('T')

time_format = "%Y-%m-%d %H:%M:%S"


class Res(GenericModel, Generic[T]):
    code: int
    msg: str
    # 表示data可以为None， 或者就是T类型 -> 使用时决定对应类型 Res[T]
    data: Optional[T]

    @staticmethod
    def success(data=None, exclude=()):
        if data is None:
            data = []
        return Res.encode_json(dict(code="000", msg="ok", data=data), *exclude)

    @staticmethod
    def error(err: BusinessCodeEnums = BusinessCodeEnums.BaseCode):
        """ 业务code """
        traceback.print_exc()
        return Res.encode_json(dict(code=err.code, msg=err.msg, ))

    @staticmethod
    def abnormal(abnormal: BusinessError):
        """ 根据异常返回 """
        traceback.print_exc()
        return Res.encode_json(dict(code=abnormal.code, msg=abnormal.msg, ))

    @staticmethod
    def encode_json(data: Any, *exclude: str):
        return jsonable_encoder(
            data,
            exclude=exclude,
            custom_encoder={datetime: lambda x: x.strftime(time_format)},
        )
