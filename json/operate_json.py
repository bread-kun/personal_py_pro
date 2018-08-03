#!/usr/bin/env python
# -*- coding:utf-8 -*-
# a little demo that operate json file in python

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

def read_json(_path, _decoder = "utf-8"):
	# check file is exist or not
	if os.path.isfile("./%s" %_path):
		_file = _path
		try:
			f = open('./%s' %_file, "r", encoding=_decoder)
			load_dict = json.load(f)
			print(load_dict)
		except UnicodeDecodeError as unicode_e:
			# if the target file is encode by gbk , here can auto chage to the gbk but only in this
			if _decoder == "utf-8":
				return read_json(_path, _decoder = "gbk")
			else:
				raise UnicodeDecodeError("未知文件编码", unicode_e)
		except json.decoder.JSONDecodeError as json_e:
			raise json.decoder.JSONDecodeError("JSON 文件格式错误", json_e)
		except Exception as e:
			raise e
		else:
			pass
		finally:
			f.close()
	else:
		print("param error!")


def main(args = sys.argv):
	if len(args) > 1:
		read_json(_path = args[1])
	else:
		raise Exception("commond error: need one more param")
	
if __name__ == '__main__':
	main()