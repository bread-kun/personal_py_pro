#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""
	pull log zip
"""
import os

def pulllog(addr=r"sdcard/Android/log", type="zip"):
	with os.popen("adb shell ls %s" %addr) as p_stream:
		_target_ = []
		readStr = p_stream.read()
		tmplist = readStr.strip().split("\n")
		for file_name in tmplist:
			if file_name[-3:] == type:
				_target_.append(file_name)
	for t_file in _target_:
		with os.popen("adb pull %(addr)s/%(file)s" %{'addr':addr, 'file':t_file}) as option:
			print("正在获取文件 %s ..." %t_file)
			pass

def main():
	pulllog()

if __name__ == '__main__':
	main()