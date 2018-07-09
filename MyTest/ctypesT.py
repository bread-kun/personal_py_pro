#!/usr/bin/env python
# this module is for learn about the use way of ctypes module
import ctypes
import time

def getProcess():
	# get current user
	current_usr = ctypes.windll.user32
	# get kernel whitch could control some process
	kernel = ctypes.windll.kernel32

	# height window , get the topest windows
	hwnd = current_usr.GetForegroundWindow()

	# get pid in c varibale type
	pid = ctypes.c_ulong(0)
	current_usr.GetWindowThreadProcessId(hwnd,ctypes.byref(pid))

	# get for memory
	executable = ctypes.create_string_buffer(b'\x00'*256)
	h_process = kernel.OpenProcess(0x400 | 0x10, False, pid)

	ctypes.windll.psapi.GetModuleBaseNameA(h_process,None,ctypes.byref(executable),256)

	# read the window title
	windows_title = ctypes.create_string_buffer(b"\x00"*256)
    length = current_usr.GetWindowTextA(hwnd,ctypes.byref(windows_title),256)
    
	return (pid,executable.value,windows_title.value,length)

def main():
	current_pid = ctypes.c_ulong(0)
	while 0:
		time.sleep(1)
		(t_pid,executable,windows_title,title_length)= getProcess()
		if current_pid.value != t_pid.value:
			current_pid = t_pid
			print("current info:\n\rpid:",current_pid,"\t ,exec:",executable,"\t ,title:",windows_title,"\t ,title_length:",length)

		pass
	

if __name__ == '__main__':
	main()