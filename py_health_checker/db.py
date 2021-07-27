#!/usr/bin/env python3
import functools, asyncio
from .utils import load_json_from_file, dump_json_to_file, create_file_if_not_exists
from .constants import DB_FILENAME, PROJECT_DIR_PATH_OBJ, DEFAULT_DB, DEFAULT_DB_TARGET
from . import logger

def save_db(func):
    @functools.wraps(func)
    def wrap(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
            asyncio.ensure_future(self._save_db())
            return result
        except Exception as e:
            logger.error(f'save_db error: {e}')
    return wrap

class DB():
    FILE_PATH = str(PROJECT_DIR_PATH_OBJ / DB_FILENAME)

    def __init__(self):
        self._data = {}
        self.init_db()
        self._load_db_from_file()

    def get_target(self, id):
        if id in self._data["targets"] and self._data["targets"][id]:
            return self._data["targets"][id]
        
        self._data["targets"][id] = DEFAULT_DB_TARGET
        return self._data["targets"][id]

    def get_all(self):
        return self._data

    @save_db
    def insert_channels(self, channels):
        self._data["channels"] = channels
        return self._data["channels"]

    @save_db
    def insert_target(self, target):
        id = target["id"]
        self.get_target(id)

        self._data["targets"][id] |= target

        return self._data["targets"][id]

    @save_db
    def update_target(self, up=None, notified=None, id=None):
        target = self.get_target(id)
        
        if up is not None:
            if target["up"] != up:
                self._data['targets'][id]["up"] = up
                self._data['targets'][id]["last_notified"] = False
                logger.log(f"target status changed: {id}. Previous status {target['up']} new status : {up}")
        
        if notified is not None:
            logger.log(f"target notified changed {notified}")
            self._data['targets'][id]["last_notified"] = notified
        
        return self._data['targets'][id]


    def init_db(self):
        created = create_file_if_not_exists(DB_FILENAME)
        if created:
            logger.log(f"Initiating default DB")
            dump_json_to_file(content=DEFAULT_DB, path_to_file=self.FILE_PATH)

    def _load_db_from_file(self):
        self._data = load_json_from_file(self.FILE_PATH)

    async def _save_db(self):
        dump_json_to_file(content=self._data, path_to_file=self.FILE_PATH)

    
    
db = DB()




