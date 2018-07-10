#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author	asange
# @editTool	sublime
# @time		2018-7-9 23:51:23
# 钩子(Hook) 类似于回调、注册，将hook函数注册、或者是类似与监听之类的到目标点上
# 说一下 hook 的机制：
#			对要扩展（暂时不扩展）的地方放置一个钩子函数，即对象本体需要有接口对接

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
				
	

class Student_Hooker(object):
	"""
		a content some hook function class
	"""
	def __init__(self):
		self.student_hook = False
		# 对实例对象的方法hook挂载
		self.student_gohome_hook = False
		self.student_study_hook = False

	def getStudent(self):
		if self.student_hook:
			return self.student

	def setStudent(self, student):
		if type(student)==Student:
			pass
			self.student = student
			self.student_hook = True

	def getGoHome(self):
		if self.student_gohome_hook:
			return self.student_gohome_hook_func

	# 设置挂载点
	def setGoHome(self, hook_func, *args, **kwargs):
		if self.student_hook is False:
			return;
		self.student_gohome_hook_func = hook_func
		self.student_gohome_hook = True

	def getStudy(self):
		if self.student_study_hook:
			return self.student_study_hook_func

	def setStudy(self, hook_func, *args, **kwargs):
		if self.student_hook is False:
			return;
		self.student_study_hook_func = hook_func
		self.student_study_hook = True
	
	# 外界通过 register 获取设置内部方法
	# 使用方法： hooker实例.student_register = Student实例
	student_register = property(getStudent, setStudent)
	student_gohome_register = property(getGoHome, setGoHome)
	student_study_register = property(getStudy, setStudy)

	def stuRun(self):
		import time
		import random
		while 1:
			time.sleep(3)
			if random.randint(1,2) == 1:
				self.student.goHome()
				if self.student_gohome_hook:
					self.student_gohome_hook_func()
				pass
			else:
				self.student.study()
				if self.student_study_hook:
					self.student_study_hook_func()
			
def my_gohome_plugin():
	print("let's go home!!!")

def my_study_plugin():
	print("let's study!!!")


def main():
	stu = Student("Lili", 123)
	shooker = Student_Hooker()
	shooker.student_register = stu
	# 可以挂载自定义函数,差不多就是这个样，写的太复杂了些
	shooker.student_gohome_register = my_gohome_plugin
	shooker.student_study_register = my_study_plugin
	# 执行在 Hooker 上
	shooker.stuRun()

if __name__ == '__main__':
	main()
