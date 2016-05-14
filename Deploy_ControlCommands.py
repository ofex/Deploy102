#!/usr/bin/python
import threading
from socket import *

def SendRecv(SatI,Command):
	Clnt = socket(AF_INET,SOCK_STREAM)
	Clnt.connect((SatI[0], SatI[1]))
	Clnt.sendall(Command)
	if (Clnt.recv(4096) == "Successful"):
		SatI[2] = "Online"
	else:
		SatI[2] = "Not Responding"
	Clnt.close()
	
def Satalight_Status(SAList)
	cmd = "Status"
	for sal in SAList:
		sal[2] = "Verifying"
		print " -Satalight: %s\t-Port: %s\t-Status: %s " % (sal)
		threading.Thread(target=SendRecv,args=(sal,cmd,)).start():

		