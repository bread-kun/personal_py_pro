#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 协程，微线程，纤程 Coroutine 
# 功能：可以在一个子程序(函数)中运行中断转而去执行其他子程序(其他函数)
# 特点：无需子程序(函数)相互调用
#		比线程级别低
#		在一个线程中执行，并且可以有多个
# 注意：python 本身仅通过yield 实现对协程的基本支持
from time import sleep
from random import randint

	

def get_num_bigger(stander=20):
	rand = 0
	while True:
		_randnum = yield rand
		rand = _randnum
		if _randnum < stander:
			print("i'm wating...")
			rand = 0
		sleep(1)
	pass

"""generate ten random num bigger"""
def generate_random(consumer, r_range=(0,31), m_count=10):
	consumer.__next__()
	_g_count = 0
	while _g_count < m_count:
		_randnum = randint(r_range[0],r_range[1])
		print("Generate num:%d" %_randnum)
		_v = consumer.send(_randnum)
		# insert the consumer func
		if _v is not 0:
			_g_count += 1
			print("Generate a stander num:%d" %_v)
		sleep(2)
	# consumer.close()

def main():
	co = get_num_bigger(15)
	generate_random(co, (0, 30), 5)
	pass

if __name__ == '__main__':
	main()