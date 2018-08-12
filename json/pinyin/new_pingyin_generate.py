#!/usr/bin/env python
# -*- coding:utf-8 -*-

def generate_newpinyin():
	try:
		wr_stream = open("new_pinyin.txt","a+",encoding="utf-8")
		with open("pinyin.txt",'r+', encoding="utf-8") as f_stream:
			_inf = f_stream.readline()
			_inf = f_stream.readline()
			_inf = f_stream.readline()
			while _inf != "":
				_line_1 = _inf.split(':')
				_line_2 = _line_1[1].split("#")
				print(_line_1[0], _line_2[0], _line_2[1])
				_str_line = "{} : {} # {}\n\r".format(_line_1[0].strip(' '), _line_2[1][:-1].strip(' '), _line_2[0].strip(' '))
				wr_stream.write(_str_line)
				wr_stream.flush()
				_inf = f_stream.readline()
	except Exception as e:
		raise e
	finally:
		wr_stream.close();
	pass

def main():
	generate_newpinyin()
	pass

if __name__ == '__main__':
	main()