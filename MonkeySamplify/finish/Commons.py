#!/usr/bin/env python
from os import popen

def getDeviceList():
	serialno_list = []
	with popen("adb devices") as bufferReader:
		_read_str = bufferReader.read()
		_tmp_list = _read_str.strip().split("\n")
		_tmp_list.pop(0)
	for x in _tmp_list:
		index = x.index('\t');
		serialno_list.append(x[0:index])
	return serialno_list

def getPackageList():
	package_list = []
	with popen("adb shell pm list packages") as bufferReader:
		_read_str = bufferReader.read()
		_tmp_list = _read_str.strip().split("\n")
		_tmp_list = __stripList(_tmp_list)
	for x in _tmp_list:
		index = x.index(':');
		package_list.append(x[index+1:])
	package_list.reverse()
	return package_list

def getBattery():
	from decimal import Decimal,getcontext
	# 精度控制
	getcontext().prec = 18
	_maps = {}
	with popen("adb shell dumpsys battery") as bufferReader:
		_read_str = bufferReader.read()
		_tmp_list = _read_str.strip().split("\n")
		_tmp_list.pop(0)
		_tmp_list = __stripList(_tmp_list)
	for x in _tmp_list:
		k,v = x.strip().split(": ")
		_maps[k] = v
	return _maps

def getFlow(package_name):
	def __get_pid(package_name):
		# 进程名, pid , 父pid, 虚拟运行内存空间, 
		_title = ["USER", "PID","PPID","VSIZE","RSS","WCHAN","PC","STATU","NAME"]
		try:
			with popen("adb shell \" ps | grep %s \"" %package_name) as bufferReader:
				_read_str = bufferReader.read()
				if len(_read_str.strip()) is 0:
					# raise Exception("该应用没有启动")
					print("target package have no process")
				_tmp_list = _read_str.strip().split("\n")
				_tmp_list = __stripList(_tmp_list)
				_result = []
				for x in _tmp_list:
					_row = __stripList(x.split(" "))
					_result.append(dict(zip(_title,_row)))

		except Exception as e:
			raise e
		for x in _result:
			if (x["NAME"] == package_name):
				return x["PID"]
				
	_pid = __get_pid(package_name)

	


# 清掉数组中多余的空格与文本空格
def __stripList(t_list):
	_tmp_list = []
	for x in t_list:
		if len(x) is 0:
			continue
		if isinstance(x, str):
			if len(x.strip()) is 0:
					continue
		_tmp_list.append(x)
	return _tmp_list

def __scan_port():
	from telnetlib import Telnet
	# creat Telnet object
	server = Telnet()
	try:
		server.open("localhost","5037")
		print('{0} port {1} is open'.format('localhost','5037'))
	except ConnectionRefusedError as e:
		print('{0} port {1} is not open'.format('localhost','5037'))
		print('trying to start adb server')
		with popen("adb start-server"):
			pass
	finally:
		server.close()
	pass

def main():
	# print(getPackageList())
	getFlow("com.netease.cloudmusic")
	# print(getBattery())
	# __scan_port()

if __name__ == '__main__':
	main()
