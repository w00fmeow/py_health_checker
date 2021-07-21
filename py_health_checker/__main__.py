#!/usr/bin/env python3
import asyncio
from .cli import launch
from . import logger

def main():
    logger.info("Staring")
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(launch(loop=loop))
    loop.run_forever()


if __name__ == '__main__':
    main()