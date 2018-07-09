#!/usr/bin/env python
#encoding:utf-8
import random
from random import uniform
print(dir(random))
# [5,10)
print(int(uniform(5,10)))
print(random.random())

# shuffle the list
tlist = [1,2,3,4,5,6,7,8,9]
random.shuffle(tlist)
print(tlist)