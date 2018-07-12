#!/usr/bin/env python
# @author	asange
# @time		2018-7-12 08:49:45
# how to creat a thread? may be we can creat a decorator to make some function as a thread

import threading
from functools import wraps
import time
import random

class MyThread(object):
	"""docstring for MyThread"""
	def __init__(self):
		pass

	def __call__(self, func):
		func._thread_status = False
		@wraps(func)
		def _call(ins, *args, **kwargs):
			if not func._thread_status:
				_thread.start()
				print("thread start")
				print(ins)
				func._thread_status = True
			return func(ins, *args, *kwargs)
		_thread = threading.Thread(target=func)

		def _inner(func):
			pass
		
		return _call

## make some test
class Person(object):
	"""docstring for Person"""
	def __init__(self, arg):
		self.arg = arg

	@MyThread()
	def sayHello(self):
		while 1:
			print("Hello")
			time.sleep(random.randint(1,5))
			pass
		pass

	@MyThread()
	def sayWhat(self):
		print("What?")
		while 1:
			print("What?")
			time.sleep(random.randint(1,5))
			pass
		pass

def main():
	p = Person(123)
	p.sayWhat()
	print("after")
	p.sayHello()
	pass

if __name__ == '__main__':
	main()