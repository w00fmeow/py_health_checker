#!/usr/bin/env python3
from enum import Enum

class HTTPMethod(Enum):
    GET = 'GET'
    POST = 'POST'


class ChannelType(Enum):
    TELEGRAM = 'telegram'

class TargetType(Enum):
    HTTP = 'http'

class LogLevel(Enum):
    LOG = 'LOG'
    INFO = "INFO"
    ERROR = "ERROR"

class TimeUnit(Enum):
    SEC = "sec"
    MIN = "min"
    HOUR = "hour"
    DAY = 'day'
    WEEK = 'week'