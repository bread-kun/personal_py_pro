#!/usr/bin/env python

def getDeviceList():
	from os import popen
	serialno_list = []
	with popen("adb devices") as devices:
	readStr = devices.read()
	tmplist = readStr.strip().split("\n")
	tmplist.pop(0)
	for x in tmplist:
		index = x.index('\t');
		serialno_list.append(x[0:index])
	return serialno_list
