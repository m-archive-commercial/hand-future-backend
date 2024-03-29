"""
versions:
    2022-09-07: refactor: snake to pascal
ref: https://www.toptal.com/python/in-depth-python-logging#python-logging-best-practices
"""
import logging
import os.path
import sys
from logging.handlers import TimedRotatingFileHandler

from src.libs.path import LOGS_DIR

FORMATTER = logging.Formatter(
    # cons: too annoying when log like: `[regenerate_field.py:regenerate_field:regenerate:16]`
    # ref: https://stackoverflow.com/a/44401529/9422455
    # change log levelname length, ref: https://stackoverflow.com/questions/27453056/change-levelname-format-in-logrecord
    # '%(asctime)s, %(levelname).1s [%(filename)s:%(module)s:%(funcName)s:%(lineno)d] %(message)s'

    "%(asctime)s %(levelname).1s [%(filename)s:%(lineno)d] <%(name)s> %(message)s"
)


def getConsoleHandler(level=logging.INFO):
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    console_handler.setLevel(level)
    return console_handler


def getFileHandler(filename="track.log", level=logging.DEBUG):
    file_handler = TimedRotatingFileHandler(os.path.join(LOGS_DIR, filename), when='midnight')
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(level)
    return file_handler


def getLogger(logger_name):
    _logger = logging.getLogger(logger_name)
    _logger.setLevel(logging.DEBUG)  # better to have too much log than not enough
    _logger.addHandler(getConsoleHandler(os.getenv('LOG_LEVEL', logging.INFO)))
    _logger.addHandler(getFileHandler("out.log", logging.DEBUG))
    # with this pattern, it's rarely necessary to propagate the error up to parent
    _logger.propagate = False
    return _logger


if __name__ == '__main__':
    logger = getLogger("test")
    logger.debug("test of debug")
    logger.info("test of info")
    logger.warning("test of info")
    logger.error("test of error")
