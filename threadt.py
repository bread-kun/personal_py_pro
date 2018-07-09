#!usr/bin/env python

# 线程不能独立执行，必须依存于应用程序中，由应用程序提供多个线程执行控制
# 执行线程（_thread）的片段需要保持一直运行中，即（while 1）,否则，主体死亡，线程无可依附
# 程序亦死亡
# thread.start_new_thread ( function, args[, kwargs] )
# import _thread
# import time
# def ticks(threadName,delay):
# 	count = 0
# 	while count < 10:
# 		time.sleep(delay)
# 		print(threadName + " : " + time.localtime())
# 		count += 1
# try:
# 	_thread.start_new_thread(ticks,("thread-1",1))
# 	_thread.start_new_thread(ticks,("thread-2",2))
# 	_thread.start_new_thread(ticks,("thread-3",3))
# except:
# 	print("Error: unable to start thread")
# 	raise
# else:
# 	pass
# finally:
# 	pass
import _thread
import time

# 为线程定义一个函数
def print_time( threadName, delay = 0.01):
   count = 0
   while 1:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 创建两个线程
try:
   _thread.start_new_thread( print_time, ("Thread-1", ) )
   _thread.start_new_thread( print_time, ("Thread-2", ) )
except:
   print ("Error: 无法启动线程")
# important！！
while 1:
   pass