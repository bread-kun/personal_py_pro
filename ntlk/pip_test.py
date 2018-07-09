#!/usr/bin/env python
import subprocess

def process_test(command):
	instance = subprocess.run(command)
	#print(instance)
	return instance

def process_test_2(command):
	try:
		popens = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
	except Exception as e:
		raise e
	return popens
def main():
	# print("2")
	# instance = process_test("adb shell")
	# print(instance) -- none
	# print("2")
	p = process_test_2("adb shell")
	p.communicate("")
	pass

if __name__ == '__main__':
	main()