#!/usr/bin/env python3
import aiohttp
from datetime import datetime
from .db import db
from .constants import GLOBAL_TIMEOUT_SEC
from . import logger


async def send_telegram(config=None, message=None, target=None):
    timeout = aiohttp.ClientTimeout(total=GLOBAL_TIMEOUT_SEC)
    session = aiohttp.ClientSession(timeout=timeout)
    params = {
        "chat_id": config["chat_id"],
        "text": message
    }
    
    try:
        await session.post(f"https://api.telegram.org/bot{config['bot_id']}:{config['token']}/sendMessage", params=params)
        
        db.update_target(notified=int(datetime.now().timestamp()), id=target["id"])

        await session.close()
    except Exception as e:
        logger.error(f"send_telegram error: {e}")
        
        if session:
            await session.close()
