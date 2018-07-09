#!/usr/bin/env python
#encoding:utf-8
import os
# simple if expression
if 1 is not 2: print("1 is not 2")
print("this expression always run")

print("for expression")
string = "This is a test progress!"
# for c in string:
# 	print(c)
# range(start,[stop[,step]])
for index in range(2,len(string),3):
	print(string[index])
print(dir(os))