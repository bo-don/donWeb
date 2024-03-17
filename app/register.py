# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         : don
@Software       : PyCharm
------------------------------------
@File           :  register.py
@Description    :  工厂函数
@CreateTime     :  2024/03/10
------------------------------------
"""

from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from loguru import logger
from starlette.middleware.exceptions import ExceptionMiddleware

from app.libs.exception_handlers import (
    validation_exception_handler, http_exception_handler, business_exception_handler, general_exception_handler)
from app.libs.exceptions import BusinessError
from app.libs.response import Res
from app.router import api_router
from app.setting import settings
from app.utils.logUtil import TraceID


def register_app():
    app = FastAPI(
        title=settings.APP_TITLE,
        version=settings.APP_VERSION,
        openapi_url=settings.APP_OPENAPI_URL,
        docs_url=settings.APP_DOCS_URL,
        redoc_url=settings.APP_REDOC_URL,
        debug=settings.DEBUG
    )

    @app.middleware("http")
    async def add_security_headers(request: Request, call_next):
        """
        设置日志的全链路追踪、设置安全响应头
        :param request:
        :param call_next:
        :return:
        """

        # 设置日志的全链路追踪
        _req_id_val = str(request.headers.get('X-Request-Id', ""))
        trace_id = TraceID.set(_req_id_val)

        try:
            response = await call_next(request)

            # 添加响应头
            response.headers['X-Request-Id'] = trace_id.get()
            response.headers["Strict-Transport-Security"] = "max-age=31536000 ; includeSubDomains"

            return response
        except Exception as exc:
            logger.error(f"接口: {request.url} 异常，异常信息: {exc}")
            return Res.abnormal()

    app.add_middleware(
        ExceptionMiddleware,
        handlers={
            RequestValidationError: validation_exception_handler,
            HTTPException: http_exception_handler,
            BusinessError: business_exception_handler,
            Exception: general_exception_handler,
        }
    )

    # 路由
    app.include_router(api_router)

    return app
