#!/usr/bin/env python
def my_decorators(func):
	def dealor(*args, **kwargs):
		print("dealor get the param", *args)
		func(*args)
	return dealor

@my_decorators
def my_function(a,b):
	print(a+b)

def main():
	my_function(3,4)

if __name__ == '__main__':
	main()