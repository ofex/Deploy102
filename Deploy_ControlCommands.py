#!/usr/bin/python
import threading
from socket import *
from Deploy_ControlMemu import *

# Get a single Satellite status (to be run in a thread)
# this function tries to connect to the parameter satellite.
#============================================================================
def Get_SLiteStt(SatI,Command):
	try:
		Clnt = socket(AF_INET,SOCK_STREAM)
		Clnt.connect((SatI[0], SatI[1]))
		#raw_input("IP: %s \t PORT: %s" % (SatI[0], str(SatI[1])))
		Clnt.sendall(Command)
		sRecive = Clnt.recv(4096)
		SatI[2]=sRecive.split("!!")[0]

#		if (sRecive == "Successful"):
#			SatI[2] = "Online"
#		elif (sRecive == "Shuting"):
#			SatI[2] = "Closed"
#		else:
#			SatI[2] = "Not Responding"
	except:
		SatI[2] = "Offline"

	finally:
		Clnt.close()
		
# Check all satellites Status
#============================================================================
def Satellites_Status(SAList):
	cmd = "Status;"
	ThList = []
	mnu_ClrPrtHeader()
	
	for sal in SAList:
		sal[2] = "Verifying"
		print " -Slite: %s\t-Port: %s\t-Status: %s " % (sal[0],sal[1],sal[2])
		TH = threading.Thread(target=Get_SLiteStt,args=(sal,cmd,))
		ThList.append(TH)
		TH.start()
	raw_input("Thread exec>>>")
	
	for I in range(len(ThList)):
		ThList[I].join()
		#if ThList[I].isAlive():
		#	SAList[I][2] = "UnReachable"
		print " -Slite: %s\t-Port: %s\t-Status: %s " % (SAList[I][0],SAList[I][1],SAList[I][2])
	raw_input("Thread Done>>>")

def Send_SLiteCmd(SatI,SCommand):
	try:
		Clnt = socket(AF_INET,SOCK_STREAM)
		Clnt.connect((SatI[0], SatI[1]))
		#raw_input("IP: %s \t PORT: %s" % (SatI[0], str(SatI[1])))
		Clnt.sendall(SCommand)
		sRecive = Clnt.recv(4096)
		SatI[2]=sRecive.split("!!")[0]
		SatI[3]=sRecive.split("!!")[1]
	except:
		SatI[2] = "Offline"
	finally:
		Clnt.close()

# Send a Command to all/choesn satellites
#============================================================================
def Satellites_SendCommand(SAList):
	cmd = "Command"
	ThList = []
	SALcmd =[]
	
	Spick = mnu_PickSatallite(SAList)

	if Spick=="Q":
		raw_input("Quit selected")
		return
	elif Spick=="A": SALcmd = SAList
	else: SALcmd.append(SAList[int(Spick)])
	
	Scommand = mnu_GetCommand()
	
	#raw_input("Satallite picked>>> "+Spick)
	#return
	Scmd = cmd+"^^"+Scommand
	
	for sal in SALcmd:
		sal[2] = "Send Command"
		print " -Satellite: %s\t-Port: %s\t-Status: %s " % (sal[0],sal[1],sal[2])
		TH = threading.Thread(target=Send_SLiteCmd,args=(sal,Scmd,))
		ThList.append(TH)
		TH.start()
	raw_input("Thread exec>>>")
	
	for I in range(len(ThList)):
		ThList[I].join()
		print " -Satellite: %s\t-Port: %s\t-Status: %s " % (SALcmd[I][0],SALcmd[I][1],SALcmd[I][2])
		print SALcmd[I][3]
	raw_input("Thread Done>>>")


def Satellite_Shut(SAList):
	cmd = "Shutdown"
	ThList = []
	mnu_ClrPrtHeader()
	
	for sal in SAList:
		sal[2] = "Shut Sent"
		print " -Satellite: %s\t-Port: %s\t-Status: %s " % (sal[0],sal[1],sal[2])
		TH = threading.Thread(target=SendRecv,args=(sal,cmd,))
		ThList.append(TH)
		TH.start()

	raw_input("Thread exec>>>")
	for I in range(len(ThList)):
		ThList[I].join()
		print " -Satellite: %s\t-Port: %s\t-Status: %s " % (SAList[I][0],SAList[I][1],SAList[I][2])

	raw_input("Thread Done>>>")
