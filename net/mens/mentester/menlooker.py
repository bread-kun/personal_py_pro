#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import time
import subprocess
from adbtools import clocker,_run
"""
	should try to use yeild to let that helpful, watch on a menery stack
"""
pkg_name = "com.meizu.media.music"
men = []
@clocker
def get_men(pkg_name):
	cmd = "adb shell  dumpsys  meminfo %s" %pkg_name
	temp = []
	m = []
	# men_s = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
	men_s = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout
	s = men_s.readline().decode(encoding="utf-8")
	if s == ("No process found for: %s\r\n" %pkg_name) or s is "":
		raise Exception("target process of %s do not started!" %pkg_name)
	men_s.seek(200)
	s = men_s.readline().decode(encoding="utf-8")
	while s is not "":
		if s.strip().startswith("TOTAL"):
			for _total in re.finditer(r"\d+",s):
				return (time.strftime('%Y/%m/%d %H:%M:%S'), _total.group())
			pass
		s = men_s.readline().decode(encoding="utf-8")
		pass


def main():
	for x in range(100):
		_g_res = get_men(pkg_name)
		print(_g_res)
		# print(_g_res[0],"  -total:",_g_res[1])
		pass
	# _run("adb shell  dumpsys  meminfo %s" %pkg_name)
	pass

if __name__ == '__main__':
	main()