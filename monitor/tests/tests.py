#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2018/2/1
"""
from tzlocal import win32
import pytz

timezone = win32.get_localzone_name()
print(timezone)
tz = pytz.timezone(timezone)
print(tz)
