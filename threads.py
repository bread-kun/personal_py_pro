#！usr/bin/env python
import threading
import time
# 从 threading.Thread 继承创建一个新的子类，实例化后启动
flag = 0

class myThread(threading.Thread):
	"""docstring for myThread"""
	def __init__(self,threadID, name, delayer):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.delayer = delayer
	def run(self):
		print("Thread (" + self.name + ") starting")
		fun(self.name, self.delayer, 5)
		print("Thread (" + self.name + ") exting")


def fun(threadName, delay, counter):
    while counter:
        if flag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# creat thread instance
thread_1 = myThread(1, "One", 0.01)
thread_2 = myThread(2, "Second", 1)

# start
thread_1.start()
thread_2.start()
# thread1.join()
# thread2.join()
# print ("退出主线程")