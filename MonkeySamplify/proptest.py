#!usr/bin/env python

import os

# try:
# 	devices = os.popen("adb devices")
# 	print(devices.read())
# 	devices.close()
# except Exception as e:
# 	raise
with os.popen("adb devices") as devices:
	serialno_list = []
	readStr = devices.read()
	tmplist = readStr.strip().split("\n")
	tmplist.pop(0)
	for x in tmplist:
		index = x.index('\t');
		serialno_list.append(x[0:index])
		print(x[0:index])
	# tmplist = readStr.strip().split("\n").split("\tdevice")
	# tmplist.pop(0)
	# tmplist.remove("\tdevice")
	print(tmplist)
	print(serialno_list)
	# for x in dir(devices):
		# print("devices."+ x + " :");print(getattr(devices,x))
		# print(x + "\t:\t" + eval("devices."+x))
