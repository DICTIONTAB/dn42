#!/usr/bin/env python

import socket
import threading

class AccessCounter():
	def __init__(self):
		self.v4queries = 0;
		self.v6queries = 0;
	
	def show(self):
		print("Served {0} v4 and {1} v6 queries".format(self.v4queries, self.v6queries))

class ServerThread(threading.Thread):
	def __init__(self, address, sockettype, counter):
		threading.Thread.__init__(self)   
		self.address = address
		self.sockettype = sockettype
		self.counter = counter

	def run(self):
		print("Starting server @ " + self.address)
		serversocket = socket.socket(self.sockettype, socket.SOCK_STREAM)
		serversocket.bind((self.address, 23))
		serversocket.listen(5)
		while 1:
			(clientsocket, address) = serversocket.accept()
			clientsocket.send(address[0] + "\r\n")
			clientsocket.close()
			if(self.sockettype == socket.AF_INET):
				self.counter.v4queries += 1;
			elif(self.sockettype == socket.AF_INET6):
				self.counter.v6queries += 1;
			self.counter.show()

counter = AccessCounter()
ServerThread("172.20.58.64", socket.AF_INET, counter).start()
ServerThread("fdc1:d4b:b89a::1", socket.AF_INET6, counter).start()

print("Startup finished")
