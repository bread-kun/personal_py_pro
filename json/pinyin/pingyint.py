#!/usr/bin/env python
# -*- coding: utf-8 -*-

target = ["饿","啊","噢","㐀","我","沙","并","奥"]

def sort_pingying():
	_t_map_ = {}
	_l = []
	with open("pinyin.txt", "r", encoding="utf-8") as pinyin_dict_stream:
		strs = pinyin_dict_stream.read()
		for indx , chrs in enumerate(target):
			###################get pinyin #######
			_dex = strs.index(chrs)
			_start = 0
			_end = 0
			while strs[_dex] != ":":
				_end = (_dex if strs[_dex] is "#" else _end)
				_dex -= 1
			_start = _dex+1
			_pinyin_mark = strs[_start:_end].strip(" ")[0]
			if _pinyin_mark in ["ā","á","ǎ","à"]:
				_pinyin_mark = 'a'
			# īíǐì,ūúǔùǖǘǚǜü
			elif _pinyin_mark in ["ē","é","ě","è"]:
				_pinyin_mark = 'e'
			elif _pinyin_mark in ["ō","ó","ǒ","ò"]:
				_pinyin_mark = 'o'
			else:
				pass
			_t_map_[indx] = _pinyin_mark
			pass
			#######################################
		for l in range(0,len(target)):
			_min = list(_t_map_.keys())[0]
			for _k in _t_map_.keys():
				if _t_map_[_k] < _t_map_[_min]:
					_min = _k
			_l.append(_min)
			_t_map_.pop(_min)
		for _i, index in enumerate(_l): 
			_l[_i] = target[index]
		print(_l)
	pass

def main():
	sort_pingying()
	pass

if __name__ == '__main__':
	main()