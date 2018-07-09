#!/usr/bin/env python
#encoding:utf-8

print("逻辑运算符 and or not")

print("成员运算符 in / not in")

t_list = [1,2,3,4]

if 1 in t_list:
	print("1 in t_list")
else:
	print("1 ont in t_list")

print("身份运算符 is / not is")

print (t_list[0] is 1)
print (t_list[0] is not 2)