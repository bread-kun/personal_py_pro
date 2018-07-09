#!/usr/bin/env python
# python defult use utf-8 as encoding

# 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。
# 模块让你能够有逻辑地组织你的 Python 代码段。
# 把相关的代码分配到一个模块里能让你的代码更好用，更易懂。
# 模块能定义函数，类和变量，模块里也能包含可执行的代码。
from fun import sum
# set PYTHONPATH=c:\python27\lib;
print("Python 3 系统默认使用的就是utf-8编码。 ")
# gloabls() and locals() like the name , return the var in various feild
# reload(fun) reload() is buildin in 2 but no 3
# from importlib import fun
# importlib.reload(fun)