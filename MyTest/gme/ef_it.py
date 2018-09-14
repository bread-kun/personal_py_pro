#!/usr/bin/env python
# -*- coding:utf-8 -*-
from random import randint
effs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

"""generate a list with the length that every item have 4 effs"""
def gener(length=20,target=effs, effs_num = 3):
	items = []
	for x in range(1,length+1):
		_t = []
		for y in range(0,effs_num):
			_r = randint(0,len(target)-1)
			while target[_r] in _t:
				_r = randint(0,len(target)-1)
				continue
			_t.append(target[_r])
		items.append(_t.copy())
	return items

"""let the gener return list change to a list by effs"""
def c_gener(ls, tar=effs):
	target = {}
	for e in tar:
		target[e] = []
		for i in range(len(ls)):
			if e in ls[i]:
				target[e].append(i)
	return target

"""let the return dict of c_gener change to a table of grape"""
def c_table(target,length=20):
	# recive a list and list a list with 2 items tuple exchater
	def li_cup_tuple(ls):
		res = []
		for x in range(len(ls)):
			for y in range(x+1,len(ls)):
				if x!=y:
					res.append((ls[x],ls[y]))
		return res
	########### generate a none table ##############
	table = []
	for row in range(length):
		table.append([])
		for colm in range(length):
			table[row].append([])
	########### start to fill table ###########
	for k in target.keys():
		_cup = li_cup_tuple(target[k])
		for _x,_y in _cup:
			table[_x][_y].append(k)
			table[_y][_x].append(k)
	return table
	pass


def g_max_effs(table,item=0):
	def _effs_mix(effs_1,effs_2):
		_mix_res = effs_1.copy()
		for _t in effs_2:
			if _t not in effs_1:
				_mix_res.append(_t)
		return _mix_res

	_res = []
	for item_2 in range(len(table[item])):
		if len(table[item][item_2]) < 1:
			continue
		# _res.append({"items":[item,item_2],"effs":table[item][item_2]})
		for item_3 in range(len(table[item])):
			if len(table[item_3][item_2]) > 0 and item_3 != item and item_2 < item_3:
				_res.append({"items":[item,item_2,item_3],"effs":_effs_mix(_effs_mix(table[item][item_2],table[item_3][item_2]),table[item][item_3])})
			pass
		pass
	return _res
	pass

def table_sort(table):
	
	pass

def main():
	_len = 20
	items = gener(_len)
	print("{object_index} --> {effslist}")
	for x in range(len(items)):
		print("{}-->{}".format(x, items[x]))
	print("="*35,"{effs} --> {object_list}")
	# ==================================
	te = c_gener(items)
	for _k in te.keys():
		print("{}-->{}".format(_k,te[_k]))
	print("="*35,"table--->")
	# ==================================
	mtable = c_table(te,length=_len)
	"""
	for _x in range(len(mtable)):
		print(mtable[_x])
		# for _y in range(len(mtable)):
			# print(mtable[_x][_y])
	print("="*35)
	"""
	# ==================================
	ma = g_max_effs(mtable, 0)
	for x in ma:
		x["effs"].sort()
		print(x)
	pass


if __name__ == '__main__':
	main()