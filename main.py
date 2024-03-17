# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         : don
@Software       : PyCharm
------------------------------------
@File           :  main.py
@Description    :  
@CreateTime     :  2024/03/10
------------------------------------
"""
import uvicorn
from loguru import logger

from app.register import register_app
from app.setting import BANNER, APP_ENV, settings
from app.utils.logUtil import init_logging

# 初始化 loguru 配置
init_logging(settings.LOG_DIR, settings.LOG_FILE_NAME, settings.LOG_FILE_LEVEL)

app = register_app()

if __name__ == "__main__":
    try:
        # 启动标志
        logger.bind(name=None).opt(colors=True).success(
            f"{settings.APP_NAME} is"
            f" at <red>{APP_ENV}</red>"
        )
        logger.bind(name=None).success(BANNER)

        uvicorn.run(
            app='main:app',
            host=settings.SERVER_HOST,
            port=settings.SERVER_PORT,
            reload=settings.SERVER_RELOAD,
        )

    except Exception as e:
        logger.error(f'❌ {settings.APP_NAME} start failed: {e}')
