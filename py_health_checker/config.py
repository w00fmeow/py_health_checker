#!/usr/bin/env python3
from .utils import create_file_if_not_exists, dump_json_to_file, load_json_from_file
from .constants import DEFAULT_CONFIG_FILE_NAME, DEFAULT_CONFIG, DEFAULT_DB, DB_FILENAME, DEFAULT_CONFIG_FILE_PATH
from .validators import validate_config, validate_time_interval
from .mappings import interval_to_sec
from .import logger

def parse_config(path=None):
    if not path:
        path = create_default_config_if_not_exists()
    
    config_content = load_json_from_file(path)
    parsed_config = validate_config(config_content)
    return parsed_config

def create_default_config_if_not_exists():
    created_path = create_file_if_not_exists(file_name=DEFAULT_CONFIG_FILE_NAME)
    
    if created_path:
        dump_json_to_file(path_to_file=created_path, content=DEFAULT_CONFIG)
        return created_path

    return DEFAULT_CONFIG_FILE_PATH

def create_db_if_not_exists():
    created_path = create_file_if_not_exists(file_name=DB_FILENAME)

    if created_path:
        dump_json_to_file(path_to_file=created_path, content=DEFAULT_DB)


def parse_time_interval(input):
    [time, unit] = validate_time_interval(input)
    return interval_to_sec[unit](time)
