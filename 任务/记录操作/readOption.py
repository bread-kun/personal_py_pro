#!/usr/bin/env python
from os import popen
import _thread
"""get option from device input"""
"""
	1.get shell pip(command "getevent")
	2.read pip output info(read event4)
	3.deal info (change hex to oct)
	4.save info
"""
def getInputCommand(shell_stream):	
	command = input(">>>")
	shell_stream.write("input text %s"%command)

with popen(r"adb shell","w") as shell_stream:
	strs = "string"
	try:
		shell_stream.write("input text %s" % strs)
		# _thread.start_new_thread(getInputCommand, (shell_stream,))
	except Exception as e:
		raise e
	# while True:
	# 	print(shell_stream.read())

"""
with popen(r"adb shell getevent","r") as shell_stream:
	while True:
		info = shell_stream.read()
		print(info)
"""