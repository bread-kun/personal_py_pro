#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author	asange
# @editTool	sublime
# @time		2018-7-9 23:51:23
# 钩子(Hook) 类似于回调、注册，将hook函数注册、或者是类似与监听之类的到目标点上

class Student(object):
	"""a classes class Student"""
	def __init__(self, name, stu_id):
		super(Student, self).__init__()
		self.name = name
		self.stu_id = stu_id

	def goHome(self):
		print("student ",self.name," is going home......")

	def study(self):
		print("student ",self.name," is studying...")
				
	def stuRun(self):
		import time
		import random
		while 1:
			time.sleep(3)
			if random.randint(1,2) == 1:
				self.goHome()
				pass
			else:
				self.study()

class Student_Hooker(object):
	"""
		a content some hook function class
	"""
	def __init__(self):
		super(Hooker, self).__init__()
		self.student_hook = False

	def setStudent(self, student):
		if type(student)==Student:
			pass
			self.student = student
			self.student_hook = True

	# 外界通过 register 获取设置内部方法
	student_register = property(self.student = student)
	
	def func_hook(self):
		

	# 注册器提供注册接口
	# def register_goHome_hook(self, func_goHome):
	# 	pass

def main():
	stu = Student("Lili", 123)
	shooker = Student_Hooker()
	shooker.student_register = stu
