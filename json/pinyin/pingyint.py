#!/usr/bin/env python
# -*- coding: utf-8 -*-

target = ["我","沙","并","奥"]

def sort_pingying():
	_t_map_ = {}
	with open("pinyin.txt", "r", encoding="utf-8") as pinyin_dict_stream:
		strs = pinyin_dict_stream.read().encode("utf-8")
		for chrs in target:
			_dex = strs.index(chrs.encode("utf-8")) - 4
			# read : to # both are front of the _dex
			if pinyin_dict_stream.seekable():
				pinyin_dict_stream.seek(_dex)
				_cout_ = 0
				while pinyin_dict_stream.read(1) != ':':
					pinyin_dict_stream.seek()
					break
				print(pinyin_dict_stream.readline())
				pass
	pass

def main():
	sort_pingying()
	pass

if __name__ == '__main__':
	main()