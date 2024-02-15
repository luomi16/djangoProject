# 在 exceptions 包中，你可以创建一个或多个 Python 文件来定义自定义异常类、日志记录器配置或处理日志的函数。例如，你可以创建一个 logger.py 文件来配置日志记录器。

import logging


def get_logger(name):
    """
    配置并返回一个日志记录器
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # 设置日志级别

    # 创建一个控制台处理器并设置级别为 debug
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # 创建一个日志格式器
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # 添加处理器到记录器
    logger.addHandler(handler)
    return logger
