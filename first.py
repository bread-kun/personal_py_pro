#!/usr/bin/python
#coding:utf-8
#指定编码，确保中文注释无异常  也可以用 -*-coding:utf-8 -*- 或是 vim: set fileencoding:utf-8

import os
from subprocess import call

print("hello,meizu!")

str = raw_input()

print("input string is : "+str)

##os.system(cmd)
##这种方式只是执行shell命令,返回一个返回码(0表示执行成功,否则表示失败)

result = os.system("python hello.py")

print(result)

##os.popen(cmd)
##执行命令并返回该执行命令程序的输入流或输出流.该命令只能操作单向流（输入或者输出）,与shell命令单向交互,不能双向交互

#输出流
f_out_stream = os.popen("python hello.py")
result = f_out_stream.readlines
print(type(result),result)

#输入流
finput = os.popen("adb shell",'w')

finput.write("adb shell")
print finput
#f = call("adb shell","shell=true")
#print f