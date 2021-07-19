#!/usr/bin/env python3
from .enums import TargetType, TimeUnit, ChannelType
from .checkers import http
from .notifiers import send_telegram

target_to_method = {
    TargetType.HTTP.value : lambda target : http(
                                                path=target["endpoint"],
                                                method=target["method"],
                                                checker=target["checker"],
                                                id=target["id"])
}

channel_to_method = {
    ChannelType.TELEGRAM.value : lambda channel, message, target : send_telegram(
                                                config=channel,
                                                message=message,
                                                target=target)
}

interval_to_sec = {
    TimeUnit.SEC.value: lambda sec: sec,
    TimeUnit.MIN.value: lambda min: min * 60,
    TimeUnit.HOUR.value: lambda hour: hour * 60 * 60,
    TimeUnit.DAY.value: lambda day: day * 60 * 60 * 24,
    TimeUnit.WEEK.value: lambda week: week * 60 * 60 * 24 * 7
}