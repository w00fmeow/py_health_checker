#!/usr/bin/env python3
import asyncio
from .cli import main
from . import logger


if __name__ == '__main__':
    logger.info("Staring")
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop=loop))
    loop.run_forever()
