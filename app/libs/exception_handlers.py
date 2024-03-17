# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         : don
@Software       : PyCharm
------------------------------------
@File           :  exception_handlers.py
@Description    :  异常处理
@CreateTime     :  2024/03/16
------------------------------------
"""
import traceback

from fastapi import Request, status, HTTPException
from fastapi.exceptions import RequestValidationError
from loguru import logger
from starlette.responses import JSONResponse

from app.libs.exceptions import BusinessError
from app.libs.response import Res


async def general_exception_handler(request: Request, exc: Exception):
    """ 一般异常处理 """
    logger.error(f"接口: {request.url} 异常，异常信息: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=Res.error()
    )


async def business_exception_handler(request: Request, exc: BusinessError):
    """ BusinessError异常处理 """
    logger.error(f"接口: {request.url} 异常，异常: {exc.msg}")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=Res.abnormal(exc)
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """ 请求参数验证错误异常处理 """
    logger.error(f"接口: {request.url} 异常，异常信息: {exc}")
    traceback.print_exc()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 101,
            "msg": "参数解析失败",
        }
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    """ 请求异常处理 """
    logger.error(f"接口: {request.url} 异常，异常信息: {exc}")
    traceback.print_exc()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 500,
            "msg": "系统内部错误",
        })
