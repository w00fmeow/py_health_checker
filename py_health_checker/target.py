#!/usr/bin/env python3
import asyncio
from datetime import datetime, timedelta
from .mappings import target_to_method, channel_to_method
from .utils import run_at, get_target_id
from . import logger
from .db import db
from .queue import targets_to_notify
from .constants import SERVICE_NAME

TARGET_DOWN = "[ {service_name} ] 🚫\nTarget is down: {target_name}"
TARGET_IS_BACK = "[ {service_name} ] ✅\nTarget is back online: {target_name}"



async def check_target(target=None, interval_sec=None):
    now = datetime.now()
    date = now + timedelta(seconds=interval_sec)

    await target_to_method[target['type']](target)

    await run_at(date=date, coro=check_target(target=target, interval_sec=interval_sec))

async def add_targets(targets=None, loop=None, interval_sec=None):
    for target in targets:
        target["id"] = get_target_id(target)
        db.insert_target(target=target)

        asyncio.ensure_future(check_target(target=target,
                                            interval_sec=interval_sec))

async def run_notification_worker():
    channels = db.get_all()["channels"]
    while True:
        target = await targets_to_notify.get()       

        try:
            message = TARGET_DOWN if not target["up"] else TARGET_IS_BACK
            message = message.format(
                service_name=SERVICE_NAME,
                target_name=target["name"])

            for channel in channels:
                logger.log(f"Should notify channel: {channel}")
                coro = channel_to_method[channel["type"]](channel, message, target)

                asyncio.ensure_future(coro)
            
            targets_to_notify.task_done()

        except Exception as e:
            logger.error(f"run_notification_worker error : {e}")


