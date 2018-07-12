#!/usr/bin/env python
import threading
import time
import random

def runThread(name):
	def _job():
		while 1:
			print(_name,"is running")
			time.sleep(random.randint(1,5))
			pass
	_name = name
	_thread = threading.Thread(target=_job)
	_thread.start()

# 获取已激活的线程数
# threading.active_count()
# 查看所有线程信息
# threading.enumerate()
# 查看现在正在运行的线程[这个跟java倒是有点像]
# threading.current_thread()
# def cheak_active_count():
# 	# thread.
# 	_thread = threading.Thread(target=lamdba :{time.sleep(5);print(threading.enumerate());})
# 	_thread.start()

# 	def function():
# 		pass

def main():
	runThread("my_t")
	runThread("other_t")
	# while 1:
	pass

if __name__ == '__main__':
	main()
