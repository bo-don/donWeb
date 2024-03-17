# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         : don
@Software       : PyCharm
------------------------------------
@File           :  logUtil.py
@Description    :  日志工具函数
@CreateTime     :  2024/03/10
------------------------------------
"""
from contextvars import ContextVar
from datetime import datetime
from pathlib import Path
from uuid import uuid4

from loguru import logger

from app.utils.strUtil import StrUtil

# 使用任务 request_id 来实现全链路日志追踪
_trace_id: ContextVar[str] = ContextVar('x_trace_id', default="")  # 任务ID
_x_request_id: ContextVar[str] = ContextVar('x_request_id', default="")  # 请求ID


class TraceID(object):

    @staticmethod
    def set(req_id: str) -> ContextVar[str]:
        """
        设置请求ID，外部需要的时候，可以调用该方法设置
        Returns:
            ContextVar[str]: _description_
        """
        if StrUtil.is_not_none(req_id):
            req_id = uuid4().hex
        _x_request_id.set(req_id)
        return _x_request_id

    @staticmethod
    def set_trace(req_id: str, title: str = "task") -> ContextVar[str]:
        """
        设置全链路追踪ID
        Returns:
            ContextVar[str]: _description_
        """
        if StrUtil.is_not_none(req_id):
            req_id = f"{title}:{req_id}"
        else:
            req_id = f"{title}:{uuid4().hex}"
        _trace_id.set(req_id)
        return _trace_id


def _logger_filter(record):
    record['trace_msg'] = f"{_x_request_id.get()} | {_trace_id.get()}"
    return record['trace_msg']


def init_logging(log_dir, log_file_name, log_file_level='INFO'):
    """
    初始化 loguru 配置

    日志级别：
        TRACE > DEBUG > INFO > SUCCESS > WARNING > ERROR >CRITICAL
    :return:
    """
    # 去除默认控制台输出
    # logger.remove()

    # 日志格式
    log_format = "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {trace_msg} | {name}:{function}:{line} - {message}"

    logger.add(
        Path(log_dir, f'{log_file_name}_{datetime.now().date()}.log'),
        rotation="50 MB",
        encoding='utf-8',
        retention='7 days',
        enqueue=True,
        backtrace=True,
        filter=_logger_filter,
        format=log_format,
        level=log_file_level
    )
