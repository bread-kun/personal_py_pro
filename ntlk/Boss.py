#!/usr/bin/env python

class Boss():
	"""docstring for Boss"""
	def __init__(self, name, bisness):
		self.name = name
		self.bisness = bisness
	def displayBoss(self):
		print("Boss: Name:" + self.name ,"\t, bisness:" + self.bisness)
