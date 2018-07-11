#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author	asange
# @editTool	sublime
# @time		2018-7-11 08:47:48

# 测试点，只要是方法(带返回方法)都能作为装饰器
#	测试结果：如果由不带返回方法的装饰器装饰，方法将无法调用，成为NoneType
def mydec_1(func):
	# print("只要是方法都能作为装饰器,无论目标函数是否运行，装饰器总会运行")
	print("function(with a param to recive func var) can be decorator, \n\rwhatever aim function have run or not, i aways will run")
	def mydec_1_inner(*args):
		func(*args)
		print("mydec_1_inner in running")
	return mydec_1_inner


@mydec_1
def my_func():
	print("my function")

	


##############################################################################
# 测试点，变量也可以被装饰
#	测试结果：变量无法被装饰，SyntaxError：invalid syntax
def mydec_2(param):
	return param+1

def my_func2():
	# @mydec_2
	my_var = 36;
	print(my_var)
	pass




##############################################################################
# 测试点，函数内部变量可以被改变（如：添加函数，修改变量）
# 		测试结果：无法修改函数内的变量(肯定不行的啦，变量本身就没有存在，当对象执行时才会存在的变量，如果改为使用静态变量的话，或许可行,又或者说在装饰器中使用特定添加的属性对象)
#				 
from functools import wraps
def mydec_3(func):

	def mydec_change_way():
		print("mydec_change_way")

	# 保持函数的原有名/调用名
	@wraps(func)
	def mydec_3_inner(*args, **kwargs):
		# 修改变量
		# print(dir(func))
		# func.my_var = 25
		# print(func.my_var)
		# func(*args, **kwargs)
		# print(dir(func))

		# 修改方法
		func.new_func = mydec_change_way
		func.new_func()
		func()
	return mydec_3_inner

@mydec_3
def my_func3():
	# @mydec_2
	my_var = 36;
	def my_func3_inner():
		print("my_func3_inner")
	print(my_var)
	pass

##############################################################################
# 测试点，仿制一个@property，对象的 set方法设置使用 @@property设置的方法名.setter
# 		测试结果：
#
def mydec_4(func,set_func=None):

	def setting(set_func):
		def set_inner(var):
			pass
		return set_inner
	@wraps(func)
	def mydec_4_inner(*args, **kwargs):
		func.setting = property(func, set_func)
	return mydec_4_inner		

class my_func4(object):
	"""docstring for my_func4"""
	def __init__(self, arg=36):
		self.arg = arg
		
	@mydec_4
	def _var(self):
		return self.my_var

	# @_var.setting
	def set_var(self, value):
		self.my_var = value

def main():
	# print("what is that")
	# 测试点——1
	# my_func()

	# 测试点——2
	# my_func2()

	# 测试点——3
	# my_func3()

	# 测试点——4
	my_func4()

if __name__ == '__main__':
	main()