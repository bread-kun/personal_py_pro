#!/usr/bin/env python

import nltk

"""
	对结果dict进行排序
	type 默认升序,0降序
"""
def sortDict(dict, type=1):
	# get the copy that sorted by key's character
	items = sorted(dict.items())
	t_dict = {key:value for key, value in items}
	result = {}
	for c in iter(dict):
		m_key = next(iter(t_dict.keys()))
		for key in t_dict.keys():
			if type == 1:
				m_key = (key if t_dict.get(key) > dict.get(m_key) else m_key)
			elif type == 0:
				m_key = (key if t_dict.get(key) < dict.get(m_key) else m_key)
		result[m_key]= t_dict.get(m_key)
		if m_key in t_dict:
			t_dict.pop(m_key)
	return result


			
def main():
	fdlist = []
	result = {}
	with open("Demon Song.txt") as song:
		fdlist = nltk.word_tokenize(song.read())
	# print(fdlist)
	for x in fdlist:
		if result.get(x)!=None:
			result[x] += 1
		else:
			result[x] = 1
	list = sortDict(result,0)
	dir(list)
	print(list)

if __name__ == '__main__':
	main()