#!/usr/bin/python
from sys import *
import threading
import os
from socket import *

nPORT = int(argv[1]) #24441
#nIP = "10.0.0.44"
tSTOP = threading.Event()

def DoCMD(client):
	cmData = client.recv(4096)
	print "> ",cmData, "\n"

	# Do the requested Action
	#============================================================================
	Rcmd = cmData.split("^^")[0]

	if Rcmd == "Shutdown":
		Answer = "Shuting!!"
	elif Rcmd == "Status":
		Answer = "Online!!"
	elif Rcmd == "Command":
		Answer = Slite_RunCmd(cmData.split("^^")[1])
	else:
		Answer = "Unknown"
	print ">>> ", Answer

	client.sendall(Answer)
	client.close()
	
	if Answer == "Shuting": tSTOP.set()

def Slite_RunCmd(OScmd):
	OScmd += " 2>&1"
	with os.popen(OScmd) as Fcmd: osAns = Fcmd.read()
	return("Answer!!"+osAns)


#########################################################
# Main Program
	
Slite = socket(AF_INET,SOCK_STREAM)
Slite.bind(("0.0.0.0",nPORT))
Slite.listen(100)

while not tSTOP.isSet():
	mClient,addr = Slite.accept()   # Slite accept the session here 
									# the code will wait until someone connect
	threading.Thread(target=DoCMD,args=(mClient,)).start()	
	print addr
	tSTOP.wait(0.3)

print "Closing............\n\n"
Slite.close()                          # Slite close

