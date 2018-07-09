#!usr/bin/env python
# -*- coding: UTF-8 -*-

a = 2;b = 2.6; c = "65"; d = "what"; f = None
print(int(b))		# 后边的参数代表进制，可忽略
# print(long(c,7))  # there is no more long in python 3.0
print(float(a),type(a))		# it will not change orign var , just return a new type var
print(complex(b,3))   # or complex("1+2j")
print(type(a),str(a))
print(str(b))
print(type(repr(d)))	# 将对象 x 转换为表达式字符串
print(eval("pow(3,a)"))
print(set(d))
f = frozenset(c)
print(f)		# the var is be frozen
print(dir(f))
print(chr(74))		# change an int to be a char
# print(unichr(74))  in python 3.0 is no more unichr
print(ord('J'))
#hex()/oct() 
