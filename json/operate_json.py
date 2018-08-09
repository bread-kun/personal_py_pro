#!/usr/bin/env python
# -*- coding:utf-8 -*-
# a little demo that operate json file in python
# @author asange
# @time 2018-8-8 09:22:26

import json
import sys
import os

# check the commond line param which name
def __check_file(args = sys.argv):
	for _file in args:
		if os.path.isfile("./%s" %_file):
			print("%s is in the current directory" %_file)
		else:
			print("%s is in not exist" %_file)

# defult in current path
# @param _decoder  coding for read file
# @param _path 		current page file path, defult plus signal "./"
# @return  load_dict the file json with dict type
def read_json(_path, _decoder = "utf-8"):
	# check file is exist or not
	if os.path.isfile("./%s" %_path):
		_file = _path
		try:
			f = open('./%s' %_file, "r", encoding=_decoder)
			load_dict = json.load(f)
			return load_dict
		except UnicodeDecodeError as unicode_e:
			# if the target file is encode by gbk , here can auto chage to the gbk but only in this
			if _decoder == "utf-8":
				return read_json(_path, _decoder = "gbk")
			else:
				raise UnicodeDecodeError("未知文件编码", unicode_e)
		except json.decoder.JSONDecodeError as json_e:
			print("JSON 文件格式错误,请检查文件格式是否有误")
			raise json_e
		except Exception as e:
			raise e
		finally:
			f.close()
	else:
		print("param error!")

# @param dict 	recive a dict type param to generate a new file which have order by first level dict key
# @return scussee or not
def sort_json(json_dict):
	if len(json_dict) < 1 or type(json_dict) != dict:
		raise Exception("文件为空")
	_dict = {}
	_list = list(json_dict.keys())
	# warning : sort() have no return any value
	_list.sort()
	try:
		# order dict
		for _k in _list:
			_dict[_k] = json_dict[_k]
		_f = open('./sorted_json.json',"w+", encoding="utf-8")
		json.dump(_dict, _f)
	except Exception as e:
		raise e
	finally:
		_f.close()
		pass
		


def main(args = sys.argv):
	if len(args) > 1:
		load_dict = read_json(_path = args[1])
		sort_json(load_dict)
		# print(load_dict["wifi"][0]["account"])
		# print(load_dict["wifi"][0]["password"])
	else:
		raise Exception("commond error: need one more param")
	
if __name__ == '__main__':
	main()