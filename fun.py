#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math
# 缺省参数需在最后
def calculates(a, func,b = 2):
	c = func(a,b)
	return c;

def getVartuple(arg, *tupls):
	# 用 * 号的变量名会存放所有未命名的变量参数。不定长参数
	for x in tupls:
		print(x)
	return;
# you can deliver a function
# and, you can ignore one or more param
print(calculates(3 , math.pow))
getVartuple(5,4,3,"ha",2.56)

# 匿名函数 lambda
sum = lambda a, b = 3: a + b

print(sum(3))

# 变量作用域
mains = 0
sum(mains)
print(mains)