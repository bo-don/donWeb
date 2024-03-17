# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         : don
@Software       : PyCharm
------------------------------------
@File           :  router.py
@Description    :  主路由
@CreateTime     :  2024/03/11
------------------------------------
"""
from fastapi import APIRouter

from app.libs.response import Res
from app.setting import settings

api_router = APIRouter(prefix=settings.APP_API_HEADER)



# include_in_schema=False 隐藏接口
@api_router.get("/healthcheck", include_in_schema=False)
def healthcheck():
    return Res.success()
