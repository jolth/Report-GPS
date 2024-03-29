#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Jorge A. Toro [jolthgs@gmail.com]
#

import sys, os
import socket
import threading
import time


#FILE='/tmp/gps.log'
FILE='gps.log'


def createFile(File):
	""" Create file of Log """
	with open(File, 'w') as  f:
		if f.tell() == 0: 
			print >> f, 'ID'.center(8), 'IP,Port'.center(24), 'Date'.center(12), 'Time'.center(10), 'Event'.center(7), 'Latitude'.center(10), 'Length'.center(12), 'Geocoding'.center(36)
			print >> f, ('-'*6).ljust(8), ('-'*22).ljust(24), ('-'*10).ljust(12), ('-'*8).ljust(10), ('-'*6).ljust(6), ('-'*10).ljust(10), ('-'*10).ljust(12), ('-'*34).ljust(36) 
	return True


class Device(threading.Thread):
	""" """

	endfile = 0

	def __init__(self, data, address, lock):
		threading.Thread.__init__(self)
		self.data, self.address = data, address
		self.lock = lock


	def run(self):
		self.lock.acquire(True)
		with open(FILE, 'a+') as f:
			f.seek(self.__class__.endfile)
			#print >> f, f.tell()
			#print >> f, time.asctime() + ': ' + repr(self.address)
			print >> f, ('None').ljust(8), (repr(self.address)).ljust(26), (time.strftime('%D')).ljust(12), (time.strftime("%H:%M:%S")).ljust(10), \
			('None').ljust(6), ('None').ljust(10), ('None').ljust(12), ('None').ljust(36) 
			#print >> f, self.data
			self.__class__.endfile = f.tell() 
			#f.close()
		self.lock.release()



if __name__ == "__main__":
	#if os.path.exists(FILE) or createFile(FILE):
	if createFile(FILE):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.bind((socket.gethostbyname(socket.gethostname()), 59000))

		lock = threading.Lock()
		while 1:
			try:
				data, address = sock.recvfrom(4096)
				d = Device(data, address, lock)
				d.start()
			except KeyboardInterrupt: 
				sys.stderr.write("Exit, KeyboardInterrupt\n")
				break

