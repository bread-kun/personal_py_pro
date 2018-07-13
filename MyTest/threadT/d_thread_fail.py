#!/usr/bin/env python
# @author	asange
# @time		2018-7-12 08:49:45
# how to creat a thread? may be we can creat a decorator to make some function as a thread

import threading
from _thread import start_new_thread
from functools import wraps
import time
import random

class MyThread(object):
	"""docstring for MyThread"""
	def __init__(self):
		self._thread_list = []
		print(self)
		pass

	def __call__(self, func):
		func._thread_status = False
		if func not in self._thread_list:
			func._thread_id = len(self._thread_list)
			self._thread_list.append({"func":func})
		self._thread_list[func._thread_id]["thread"] = threading.Thread(target=func)
		def _start_():
			self._thread_list[func._thread_id]["thread"].start()
			pass
		# 由别的方法来开启，不然会循环开启线程异常
		func.start = _start_
		print(func)
		@wraps(func)
		def _call(ins, *args, **kwargs):
			if not func._thread_status:
				print("")
				func._thread_status = True
			return func(ins, *args, **kwargs)
		
		print(func._thread_id)

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
	p.sayWhat.start()
	p.sayHello.start()
	pass

if __name__ == '__main__':
	main()