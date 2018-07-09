#!usr/bin/env python
# -*- coding: UTF-8 -*-

## list / tuple / dictionary ##
tlist = [1,2,3,4,5]
tlist1 = range(1,9)
print("tlist:\t",tlist)
print("tlist1:\t",tlist1,"\t type(tlist1):",type(tlist1))

ttuple = (1,)
ttuple1 = ("阿三",23.2,66, [5,4,8])
print("ttuple:\t",ttuple)
print("ttuple1:\t",ttuple1)
## error is happing in complete , not runtime, so the next can't be use
# try:
# 	ttuple1[0] = 'c'
# 	print("finish change world :",ttuple1)
# except Exception as e:
# 	print("can't change tuple's info,even string")
# 	raise
# else:
# 	pass
# finally:
# 	pass
## but , we also can change the inner list
ttuple1[3][1:3] = [5,5]
print("inner list can be change")
print("ttuple1:\t",ttuple1)

print("dictionary like map")
dict = {}
dict['one'] = "The one"
dict[2] = "the second"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
print(dict['one']    )  # 输出键为'one' 的值
print(dict[2]        )  # 输出键为 2 的值
print(tinydict       )  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值