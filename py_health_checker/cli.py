#!/usr/bin/env python3
import argparse, asyncio
from .config import parse_config, parse_time_interval
from .target import add_targets, run_notification_worker
from .db import db

parser = argparse.ArgumentParser(description="Monitor web server uptime")

parser.add_argument("-c", "--config", help='Path to config file')
parser.add_argument("-e", "--every", help='Run health checks every x time. Example: --every="10 min"', required=True)

args = parser.parse_args()

async def main(loop=None):
    config = parse_config(path=args.config)
    interval_sec = parse_time_interval(args.every)

    
    db.insert_channels(config["channels"])

    asyncio.ensure_future(run_notification_worker())

    await add_targets(targets=config["targets"],
                    interval_sec=interval_sec,
                    loop=loop)


