#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""learn reflects on python
try to create classes by some string

we can use 
	type.__new__(typeclass, classname, superclasses, attributedict)
	type.__init__(cls, classname, superclasses, attributedict)
and use global() to get class in current env, then set attribute
"""
def createClass(classname,superclasses,functiondict):
	def base_init(self,**kwargs):
		for prototype,value in kwargs.items():
			setattr(self,prototype,value)
	if not functiondict.get("__init__"):
		functiondict["__init__"] = base_init
	return type(classname,superclasses,functiondict)

dog = createClass("Dog",(object,),{})
dog_1 = dog(Name="doge",leg=4)
print(dog_1.Name,dog_1.leg)