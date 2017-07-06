#!/usr/bin/env python3
# -*- utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
#
# 06 July, 2017
#
# Moudles: time, datetime

import time

print('time.time(): ',time.time())
print('time.localtime(): ', time.localtime(time.time()))
print('time.gmtime(): ', time.gmtime())
print('time.localtime(): ', time.localtime())
print('time.strftime: ', time.strftime('%Y-%m-%d %H:%M:%S %A %B %Z', 
    time.localtime(time.time())))

print('time.clock(): ', time.clock())
print('time.daylight:', time.daylight)
print('time.timezone: ', time.timezone)
print('time.tzname: ', time.tzname)


###############################################################################
from datetime import date
from datetime import datetime
from datetime import timedelta
from datetime import tzinfo
from datetime import timezone

print('Today is: ', date.today())
print('timedelta.min: ', timedelta.min)
print('timedelta.max: ', timedelta.max)
print('timedelta.resolution: ', timedelta.resolution)

print('datetime.today: ', datetime.today())
print('datetime.now: ', datetime.now())
print('datetime.utcnow: ', datetime.utcnow())
