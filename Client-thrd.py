#!/usr/bin/python
import threading
from socket import *

def SendRecv(client,Command):
	client.sendall(Command)
	print client.recv(4096)

	
#########################################################
# Main Program
	
mClient = socket(AF_INET,SOCK_STREAM)              # select socket type
mClient.connect(("10.0.0.44",4444))              # connect to the server

#data = raw_input("Client@deb:) ")    	  # get data from the user

for i in range(1,90):
	cmd = "ping -c 1 10.0.0."+str(i) 
	#raw_input(cmd)
	#client.sendall(cmd)
	threading.Thread(target=SendRecv,args=(mClient,cmd,)).start()	


mClient.sendall("Stop")
print "Stoping..."
mClient.close() 
