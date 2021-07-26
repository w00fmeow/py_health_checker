#!/usr/bin/env python3
import aiohttp
from .constants import GLOBAL_TIMEOUT_SEC
from . import logger


async def send_telegram(config=None, message=None, target=None):
    params = {
        "chat_id": config["chat_id"],
        "text": message
    }
    
    timeout = aiohttp.ClientTimeout(total=GLOBAL_TIMEOUT_SEC)
    session = None
    try:
        session = aiohttp.ClientSession(timeout=timeout)
        await session.post(f"https://api.telegram.org/bot{config['bot_id']}:{config['token']}/sendMessage", params=params)
        
        await session.close()
    except Exception as e:
        logger.error(f"send_telegram error: {e}")
        
        if session and not session.closed:
            await session.close()
        