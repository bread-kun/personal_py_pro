#!/usr/bin/env python
# @author	asange
# @time		2018-7-13 23:21:30
# how to creat a thread? may be we can creat a decorator to make some function as a thread

import threading
from functools import wraps
import time
import random

""" decorator with param """
""" may be it was simple , but it work it """
def MyThread(loop = False, sleep = 0):
	def _func_call_(func):
		def _target_(*args, **kwargs):
			return func(*args, **kwargs)

		@wraps(func)
		def _caller_(*args, **kwargs):
			return threading.Thread(target=_target_, args=args, kwargs = kwargs)
		return _caller_
	return _func_call_

## make some test
class Person(object):
	"""docstring for Person"""
	def __init__(self, arg):
		self.arg = arg

	@MyThread(arg_1 = "haha")
	def sayHello(self):
		while 1:
			print("Hello")
			time.sleep(random.randint(1,5))
			pass
		pass

	@MyThread(arg_2 = "???")
	def sayWhat(self):
		print("What?")
		while 1:
			print("What?")
			time.sleep(random.randint(1,5))
			pass
		pass

""" how to use, just decorate you func or method , then use start() to run it as a function """
def main():
	p = Person(123)
	p.sayWhat().start()
	p.sayHello().start()
	pass

if __name__ == '__main__':
	main()