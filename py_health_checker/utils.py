#!/usr/bin/env python3
import json, asyncio, uuid
from pathlib import Path
from .constants import PROJECT_DIR_PATH_OBJ, ONE_DAY_IN_SEC
from datetime import datetime
from . import logger
from .enums import TargetType

if not PROJECT_DIR_PATH_OBJ.exists():
    PROJECT_DIR_PATH_OBJ.mkdir()

def create_file_if_not_exists(file_name=None):
    path_obj = PROJECT_DIR_PATH_OBJ / file_name
    
    if not path_obj.exists():
        path_obj.touch()
        return str(path_obj)
    return

    
def dump_json_to_file(content=None, path_to_file=None):
    file = open(path_to_file, 'w')
    file.write(json.dumps(content, indent=2, sort_keys=True))
    file.close()

def load_json_from_file(path):
    file = open(path, 'r')
    content = file.read()
    return json.loads(content)

async def wait_for(date):
        # sleep until the specified datetime
        while True:
            now = datetime.now()
            remaining = (date - now).total_seconds()

            if remaining < ONE_DAY_IN_SEC:
                break

            await asyncio.sleep(ONE_DAY_IN_SEC)
        await asyncio.sleep(remaining)

async def run_at(date=None, coro=None):
        await wait_for(date)

        try:
            return await coro
        except asyncio.CancelledError:
            logger.error("Task canceled")

def get_target_id(target):
    # TODO refactor 'target_identifier' to support other target types
    target_identifier = f"{target['endpoint']}-{target['method']}" if TargetType.HTTP.value == target['type'] else ""
    string_to_encode = f"{target['type']}-{target_identifier}"

    return str(uuid.uuid3(uuid.NAMESPACE_URL, string_to_encode))
