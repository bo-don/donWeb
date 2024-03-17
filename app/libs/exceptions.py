# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         : don
@Software       : PyCharm
------------------------------------
@File           :  exceptions.py
@Description    :  常用的响应异常
@CreateTime     :  2024/03/11
------------------------------------
"""

from typing import Any

from fastapi import HTTPException
from starlette.background import BackgroundTask

from app.libs.enums import BusinessCodeEnums


class HTTPError(HTTPException):
    def __init__(self, *, code: int, msg: Any = None, headers: dict[str, Any] | None = None):
        super().__init__(status_code=code, detail=msg, headers=headers)


class BaseExceptionMixin(Exception):
    def __init__(self, *, code: int, msg: str = None, data: Any = None,
                 background: BackgroundTask | None = None):
        self.code = code
        self.msg = msg
        self.data = data if data is not None else []
        # The original background task: https://www.starlette.io/background/
        self.background = background


class BusinessError(BaseExceptionMixin):
    def __init__(self, err: BusinessCodeEnums = BusinessCodeEnums.BaseCode, data: Any = None):
        super().__init__(code=err.code, msg=err.msg, data=data)
