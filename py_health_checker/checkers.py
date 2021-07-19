#!/usr/bin/env python3
import aiohttp, functools
from .constants import GLOBAL_TIMEOUT_SEC, DEFAULT_HTTP_METHOD, RECHECK_TARGET_BEFORE_NOTIFY
from .enums import HTTPMethod
from .queue import targets_to_notify
from . import logger
from .db import db


def notify_on_fail(func):
    @functools.wraps(func)
    async def wrap(*args, **kwargs):
        up = await func(*args, **kwargs)
        should_issue_notification = False
        db.update_target(up=up, id=kwargs["id"])
     
        if not up:
            logger.log(f"Checked failed for target: {kwargs['id']}. Rechecking")

            for _ in range(RECHECK_TARGET_BEFORE_NOTIFY):
                up = await func(*args, **kwargs)
                if up:
                    return

            logger.info(f"Target {kwargs['id']} appears to be down")
            target = db.get_target(kwargs["id"])

            should_issue_notification = not target["last_notified"]

        else:
            target = db.get_target(kwargs["id"])
            should_issue_notification = up and not target["last_notified"]

        
        if should_issue_notification:
            logger.info(f"Issuing notifications for target {kwargs['id']}")
            targets_to_notify.put_nowait(target)

        return up
    return wrap

@notify_on_fail
async def http(path=None, method=None, cookie=None, headers=None, checker=None, id=None):
    logger.info(f"Checking {path}")
    headers = None
    cookies = None
    method = HTTPMethod.GET if method == HTTPMethod.GET.value else DEFAULT_HTTP_METHOD
    session = None
    try:
        timeout = aiohttp.ClientTimeout(total=GLOBAL_TIMEOUT_SEC)
        session = aiohttp.ClientSession(timeout=timeout, headers=headers, cookies=cookies)
        response = await getattr(session, method.value.lower())(path)
       
        if checker:
            if 'status_code' in checker and checker["status_code"]:
                assert response.status == checker["status_code"]
                logger.info(f"Check passed for endpoint {path}: 'status_code == {checker['status_code']}'")

        await session.close()
        return True
    except Exception as e:
        if session:
            await session.close()

        logger.error(f"http checker error: {e}")
        return False


