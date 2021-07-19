#!/usr/bin/env python3
from .constants import SERVICE_NAME
from .enums import LogLevel

def _logger(message=None, level=LogLevel.LOG):
    print(f"[ {SERVICE_NAME} ] - {level.value}: {message} ")

def log(message):
    level = LogLevel.LOG
    _logger(message=message, level=level)

def info(message):
    level = LogLevel.INFO
    _logger(message=message, level=level)

def error(message):
    level = LogLevel.ERROR
    _logger(message=message, level=level)
