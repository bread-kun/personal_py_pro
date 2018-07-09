#!/usr/bin/env python

class Employee():

	empCount = 0	
	"""docstring for Employee"""
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def __del__(self):
		Employee.empCount -= 1
		print("销毁对象：",self.__class__.__name__,",\t ",self.name)

	def displayCount(self):
		print("总员工数：%d"%Employee.empCount)

	def displayEmployee(self):
		print("Name:",self.name, "\t,Salary:",self.salary)
