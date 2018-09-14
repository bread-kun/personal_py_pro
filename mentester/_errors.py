#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""
	content some Exception class for use adbtools
	@author asange
	@time	2018-9-12 16:07:05
"""
class NoNodeFindError(Exception):
	"""docstring for NoNodeFindError"""
	def __init__(self, target_node):
		super(NoNodeFindError, self).__init__()
		self.error_node = target_node

	def __str__(self):
		return "target node \"{error_node}\" have no avaliable in current page".format(self.error_node)
