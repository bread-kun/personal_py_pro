#!usr/bin/env python
# -*- coding: UTF-8 -*-
import time
ticks = time.time()
print(ticks)
print(dir(time))
localtimes = time.localtime()
print(dir(localtimes))
print(localtimes.tm_year)
# 格式化
print(time.asctime(localtimes))
# or
# but,why can't be chinese char?
# import locale and setlocal(locale.LC_CTYPE，"chinese")
#“在Windows里，time.strftime使用C运行时的多字节字符串函数strftime，
# 这个函数必须先根据当前locale配置来编码格式化字符串（使用PyUnicode_EncodeLocale）。
# ”如果不设置好locale的话，根据默认的"C" locale，
# 底层的wcstombs函数会使用latin-1编码（单字节编码）来编码格式化字符串，
# 然后导致题主提供的多字节编码的字符串在编码时出错。

## or you can nt.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
print(time.strftime("%Y-%m-%d  %H:%M:%S",localtimes))

from calendar import month
print("2018年5月月历")
print(month(2018,5))