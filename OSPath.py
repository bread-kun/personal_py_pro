#!/usr/bin/env python
import os

# print(dir(os))
try:
	os.mkdir("myytest")
except Exception as e:
	pass
finally:
	pass


print(os.getcwd())

os.chdir("C:\\Users\\v-yaohengpan\\Desktop")

lists = os.listdir()
# print(dir(lists))
# for x in lists:
# 	if x[0,17] == 'I have change dir':
# 		os.mkdir("I have change dir"+1)
# 	else:
# 		os.mkdir("I have change dir")
# print(lists)
dirs = []
files = []
for x in lists:
	if '.' in x:
		files.append(x)
	else:
		dirs.append(x)
print("文件列表：",files)
print("文件夹列表：",dirs)