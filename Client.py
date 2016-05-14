#!/usr/bin/python

from socket import *
	
client = socket(AF_INET,SOCK_STREAM)              # select socket type
client.connect(("10.0.0.33",4444))              # connect to the server

#data = raw_input("Client@deb:) ")    	  # get data from the user

for i in range(1,90):
	cmd = "ping -c 1 10.0.0."+str(i) 
	#raw_input(cmd)
	client.sendall(cmd)
	print client.recv(4096)                         # receive the data from the server

client.sendall("Stop")
client.close() 
