#!/usr/bin/env python3
import re, sys
from .constants import SUPPORTED_CHANNELS_SET, DEFAULT_CONFIG, CHANNEL_OBJECTS, SUPPORTED_TARGET_TYPES_SET, TARGET_OBJECTS
from . import logger
from .enums import TimeUnit, TargetType

TIME_UNIT_REGEX = re.compile(f'^([\d]+)\s({"|".join([unit.value for unit in list(TimeUnit)])})(?:s)?$')

def validate_channel(channel):
    assert isinstance(channel, object)
    
    assert "type" in channel and channel["type"]
    assert channel["type"] in SUPPORTED_CHANNELS_SET
    
    for key in CHANNEL_OBJECTS[channel["type"]]:
        assert key in channel and channel[key]

def validate_http_target(target):
    for key in TARGET_OBJECTS[target["type"]]:
        assert key in target and target[key]
    
    assert 'status_code' in target["checker"]
    assert isinstance(target["checker"]['status_code'], int)

def validate_target(target):
    assert isinstance(target, object)
    
    assert "type" in target and target["type"]
    assert target["type"] in SUPPORTED_TARGET_TYPES_SET
    
    if target["type"] == TargetType.HTTP.value:
        validate_http_target(target)
    

def validate_time_interval(input):
    try:
        res = TIME_UNIT_REGEX.search(input).groups()
        assert res

        assert len(res) == 2
        
        interval = int(res[0])
        assert interval > 0

        return [interval, res[1]]   
    except Exception:
        logger.error("Invalid time interval")
        sys.exit(1)

def validate_config(config):
    try:
        for key in DEFAULT_CONFIG.keys():
            assert key in config
        
        assert type(config["targets"]) is list
        assert type(config["channels"]) is list
        
        assert config["channels"]
        for channel in config["channels"]:
            validate_channel(channel)
        
        assert config["targets"]

        return config
    except Exception:
        logger.error("Invalid config file")
        sys.exit(1)


