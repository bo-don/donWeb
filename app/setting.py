# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         : don
@Software       : PyCharm
------------------------------------
@File           :  setting.py
@Description    :  配置文件
@CreateTime     :  2024/03/10
------------------------------------
"""
import os
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings

# 项目根目录
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BaseConfig(BaseSettings):
    """ 项目名称 """
    APP_NAME: str = 'donPro'
    APP_VERSION: str = '0.0.1'
    DEBUG: bool = False

    """ 日志路径配置 """
    LOG_DIR: str = str(Path(BASE_PATH, 'logs'))
    LOG_FILE_NAME: str = 'run'  # 日志名
    LOG_FILE_LEVEL: str = 'INFO'  # 日志级别

    """ 项目配置 """
    APP_TITLE: str = 'donPro'
    APP_API_VERSION: str = 'V1'
    APP_API_HEADER: str = f'/api/{APP_API_VERSION.lower()}'
    APP_OPENAPI_URL: str | None = None
    APP_DOCS_URL: str = f'{APP_API_HEADER}/docs'
    APP_REDOC_URL: str = f'{APP_API_HEADER}/redoc'

    MIDDLEWARE_CORS: bool = False
    MIDDLEWARE_GZIP: bool = False

    APP_ALLOWED_HOSTS: list = ["*"]

    """ 服务配置 """
    SERVER_HOST: str = '0.0.0.0'
    SERVER_PORT: int = 9000
    SERVER_RELOAD: bool = False



# 开发环境
class DevConfig(BaseConfig):
    class Config:
        env_file = Path(BASE_PATH, "conf", "dev.env")


# 线上环境
class ProConfig(BaseConfig):
    class Config:
        env_file = Path(BASE_PATH, "conf", "pro.env")


# 获取项目环境变量
APP_ENV = os.environ.get("APP_ENV", "dev")


@lru_cache
def get_config():
    """
    读取配置优化
    :return:
    """
    return ProConfig() if APP_ENV and APP_ENV.lower() == "pro" else DevConfig()


# 实例化
settings = get_config()

# DEBUG 模式判断
if settings.DEBUG:
    settings.SERVER_RELOAD = True
    settings.APP_OPENAPI_URL = f'{settings.APP_API_HEADER}/openapi.json'
    settings.LOG_FILE_LEVEL = 'DEBUG'

# 使用 pyfiglet 生成
BANNER = """
# + + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + +
#        ┏┓　　　┏┓+ +
# 　　　┏┛┻━━━┛┻┓ + +
# 　　　┃　　　　　　 ┃ 　
# 　　　┃　　　━　　　┃ ++ + + +
# 　　 ████━████ ┃+
# 　　　┃　　　　　　 ┃ +
# 　　　┃　　　┻　　　┃
# 　　　┃　　　　　　 ┃ + +
# 　　　┗━┓　　　┏━┛
# 　　　　　┃　　　┃　　　　　　　　　　　
# 　　　　　┃　　　┃ + + + +
# 　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
# 　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
# 　　　　　┃　　　┃
# 　　　　　┃　　　┃　　+　　　　　　　　　
# 　　　　　┃　 　　┗━━━┓ + +
# 　　　　　┃ 　　　　　　　┣┓
# 　　　　　┃ 　　　　　　　┏┛
# 　　　　　┗┓┓┏━┳┓┏┛ + + + +
# 　　　　　　┃┫┫　┃┫┫
# 　　　　　　┗┻┛　┗┻┛+ + + +
# + + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + ++ + + +
"""
