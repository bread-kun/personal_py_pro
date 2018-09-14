#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""
	content some function to use adb easily
	@author asange
	@time	2018-9-11 14:31:06
"""
import re
import time
# import logging
import os.path
from _errors import *
from time import sleep
from functools import wraps
from subprocess import Popen,PIPE
from xml.dom.minidom import parse,parseString

# derector for count how many time function spend
# @type		derector
def clocker(func):
	"""docstring for Clocker"""
	@wraps(func)
	def _call_(*args, **kwargs):
		_res = None
		print("===> function \'{}\' start run....".format(func.__name__))
		_start = time.clock()
		_res = func(*args,**kwargs)
		_end = time.clock() - _start
		print("===> function \'{}\' use time: {} second".format(func.__name__, _end))
		return _res
	return _call_

# run a cmd commond by Popen in shell
# @param	(str)cmd 	target commond in shell,like "adb shell getprop ***"
# @return	(Popen)_res	return the finished Popen object by the cmd
@clocker
def _run(cmd):
	_res = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True, encoding="utf-8")
	while _res.poll() is None:
		sleep(0.05)
	return _res

# dump current page xml of device, and pull remote xml file to current path
# @param  (path)default is dumtemfil in local
# @return (str)page xml
def uiautomator_dump(target="dumtemfil"):
	_res = None
	try:
		_run("adb shell uiautomator dump sdcard/{path}".format(path=target))
		_rs = _run("adb pull sdcard/{path}".format(path=target))
		while not os.path.exists(target):
			print("waiting file...")
			sleep(0.1)
		_res = open(target,'r', encoding="utf-8").read()
		return _res
	except Exception as e:
		raise e

# get the component by attribute, and return a list
# @param  (str)addr 			xml file path
#		  (str)xmlstr 			content of xml file
#		  (dict)attribute_map 	attribute-target map
# @return list(str) [x_lt,y_lt,x,y] x_left-top y_left-top x, y
def _get_component(addr='', xmlstr='', **attribute_map):
	dom = None
	if len(addr) > 1:
		dom = parse(addr)
	elif len(xmlstr) > 1:
		dom = parseString(xmlstr)
	nodes = dom.getElementsByTagName('node')
	_keys = attribute_map.keys()
	for node in nodes:
		__flag = 0
		for _k in _keys:
			if node.getAttribute(_k) != attribute_map[_k]:
				break
			__flag += 1
		if __flag == len(_keys):
			__bounds = node.getAttribute("bounds")
			return re.findall(r"\d+",__bounds)
	raise NoNodeFindError(str(attribute_map))

# get the point by component show text
# @param 	(str)find_text	the component with, such like some button with attribute text "OK"
#			(string)derection	[center,]
# @return	(list)list		the list of target component [x,y]
def getPoint(find_text, derection = "center"):
	xml = uiautomator_dump()
	_ls = [int(x) for x in _get_component(xmlstr = xml, text = find_text)]
	if derection == "center":
		return [((_ls[2]-_ls[0])//2)+_ls[0],((_ls[3]-_ls[1])//2)+_ls[1]]
	return _ls[2:]

# send a click to remote device
# @param	(list/tuple)point 	[x,y]/(x,y)
# 			(string)derection	[center,]
def click(point):
	# logging
	_run("adb shell input tap {x} {y}".format(x=point[0],y=point[1]))
	print("{_time} : click position {_x} {_y}".format(_time = time.asctime, _x=point[0], _y=point[1]))
	pass

# send a string to remote device
# @param	(string)text
def enter(string):
	_run("adb shell input tap {x} {y}".format(x=point[0],y=point[1]))
	print("{_time} : input text \"{text}\"".format(_time = time.asctime, text = string))
	pass

def u_click(string, derection = "正中间"):
	if string != '':
		if derection == "正中间":
			click(getPoint(string, "center"))
		pass
	pass

def u_input(string):
	if string != '':
		if derection == "正中间":
			click(getPoint(string, "center"))
		pass
	pass
# use chinese to code
点击 = u_click
计时 = clocker