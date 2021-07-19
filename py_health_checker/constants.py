#!/usr/bin/env python3
from .enums import HTTPMethod, ChannelType, TargetType
from pathlib import Path


PROJECT_DIR_NAME = '.py_health_checker'
DEFAULT_CONFIG_FILE_NAME = 'config.json'
DB_FILENAME = 'db'

TELEGRAM_CHANNEL = {
	"bot_id": "000000000",
	"token": "AAAAAAAAAAAAAAAAA-AAAAAAAAAAAAAAAAA",
	"chat_id": "000000000"
}

CHANNEL_OBJECTS = {
    ChannelType.TELEGRAM.value: TELEGRAM_CHANNEL
}

HTTP_TARGET = {
	"name": "Google",
    "endpoint": "https://google.com",
    "method": "GET",
    "checker": {
    	"status_code": 200
    }
}

TARGET_OBJECTS = {
    TargetType.HTTP.value: HTTP_TARGET
}

DEFAULT_CONFIG = {
    "targets": [],
    "channels": []
}

DEFAULT_DB = {
    "targets": {},
    "channels": {}
}

DEFAULT_DB_TARGET = {
    "up": True,
    "last_notified": None
}

GLOBAL_TIMEOUT_SEC = 20

DEFAULT_HTTP_METHOD = HTTPMethod.GET

SUPPORTED_CHANNELS_SET = set([channel.value for channel in list(ChannelType)])
SUPPORTED_TARGET_TYPES_SET = set([target.value for target in list(TargetType)])


home = Path.home()
PROJECT_DIR_PATH_OBJ = home / PROJECT_DIR_NAME

DEFAULT_CONFIG_FILE_PATH = str(PROJECT_DIR_PATH_OBJ / DEFAULT_CONFIG_FILE_NAME)

SERVICE_NAME = "health-checker"


ONE_DAY_IN_SEC = 60*60*24

RECHECK_TARGET_BEFORE_NOTIFY = 3