#!/usr/bin/python
import threading
import time
from socket import *

nPORT = 24444
nIP = "10.0.0.44"

#########################################################
# Functions

def SendCMD(Command):
	tClnt = socket(AF_INET,SOCK_STREAM)			# select socket type
	tClnt.connect((nIP,nPORT))					# connect to the server

	print ">",Command,"\n"
	tClnt.sendall(Command)
	print tClnt.recv(4096),"\n\n"
	tClnt.close()
	
#########################################################
# Main Program

#data = raw_input("Client@deb:) ")    	  # get data from the user

for i in range(1,90):
	cmd = "ping -c 1 10.0.0."+str(i) 
	threading.Thread(target=SendCMD,args=(cmd,)).start()	

#time.sleep(10)
#print "Sleep 10......"

cmd = "Stop"
threading.Thread(target=SendCMD,args=(cmd,)).start()
#time.sleep(1)
#threading.Thread(target=SendCMD,args=(cmd,)).start()

print "Stoping..."

