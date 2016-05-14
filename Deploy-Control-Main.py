#!/usr/bin/python
import threading
from Deploy_ControlMemu import *

from Deploy_ControlCommands import *

#####################################################
# Globals
SATAList = [["10.0.0.44",8010,"Status"],["10.0.0.44",8020,"Status"],["10.0.0.44",8030,"Status"]]

#####################################################
# Main Program
mmOption = "Go"

#Deply_Control_Setup()

while mmOption not in "qQ":
	
	mmOption = Get_mmOption()

	# Manage Clients
	##########################################
	if mmOption == "1":
		raw_input("Doing Option 1>")
		Satalight_Status(SATAList)
	elif mmOption == "2":
		raw_input("Doing Option 2>")	
	elif mmOption == "3":
		raw_input("Doing Option 3>")	
	elif mmOption == "4":
		raw_input("Doing Option 4>")	
	elif mmOption == "5":
		raw_input("Doing Option 5>")

#Deploy_Control_Close()

print "Goodbye...\n"


