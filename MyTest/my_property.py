#!/usr/bin/env python

from functools import wraps
class my_property(object):
	"""docstring for my_property"""
	# @staticmethod
	# 如果使用 @my_property 做装饰的话，由于 __init__ 最多明置返回None(默认返回my_property实例)
	# 	这样,当 目标实例的方法指向被改为 my_property[这或许可以作为一种封装方法]
	# def __init__(self, func, *args):
	# 	print("__init__")
	# 	self.func = func
	# 	def _call(*fargs):
	# 		print(fargs)
	# 		return self.func()
	def __init__(self):
		pass

	def __call__(self, func, *args):
		func.setter = self.__setter__
		@wraps(func)
		def _call_(ins,*args):
			return func(ins,*args)
		# func = property(_call_, self.__setter__)
		return _call_

	def __setter__(self, func):
		@wraps(func)
		def _call_(ins, *args):
			func(ins, *args)
		return _call_


class C(object):
	"""docstring for C"""
	def __init__(self, *arg):
		self._x = arg[0]

	@my_property()
	def getx(self):
		return self._x

	@getx.setter
	def setx(self, value):
		self._x = value


def main():
	ins = C(36)
	# 需要调用一次后才有 my_property 方法
	ins.getx()
	print(ins.getx)
	ins.setx(10)
	print(ins.getx())


if __name__ == '__main__':
	main()

# 两个变量指向同一个方法，后边的是否能改变原来的数据,--可以