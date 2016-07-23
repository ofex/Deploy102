#!/usr/bin/python
import threading

from Deploy_ControlMemu import *
from Deploy_ControlCommands import *

#####################################################
# Globals
SATAList = [["10.0.0.44",24441,"Status","Empty"],
			["10.0.0.44",24442,"Status","Empty"],
			["10.0.0.44",24443,"Status","Empty"]]
#SATAList = [["10.0.0.44",24441,"Status"],["10.0.0.44",24442,"Status"]]

#####################################################
# Main Program
mmOption = "Go"

#Deply_Control_Setup()

while mmOption not in "qQ":
	
	mmOption = mnu_GetOption()

	# Manage Clients
	##########################################
	if mmOption == "1":
		raw_input("Doing Option 1>")
		Satellites_Status(SATAList)
	elif mmOption == "2":
		raw_input("Doing Option 2>")	
		Satellites_SendCommand(SATAList)
	elif mmOption == "3":
		raw_input("Doing Option 3>")	
	elif mmOption == "4":
		raw_input("Doing Option 4>")	
	elif mmOption == "5":
		raw_input("Doing Option 5>")
	elif mmOption == "6":
		raw_input("Doing Option 6>")
		Satellite_Shut(SATAList)

#Deploy_Control_Close()

print "Goodbye...\n"


