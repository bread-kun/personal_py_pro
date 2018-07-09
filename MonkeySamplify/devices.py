#!usr/bin/env python
import os
class Device:
	"""show some device info for the flow"""
	def __init__(self, deviceSerialno):
		self.serialno = deviceSerialno
		with prop as os.popen("adb -s" + self.serialno + "shell getprop"):
			self.prop = arg
	def printDeviceInfo():
		pass
