#!/usr/bin/python
import threading
<<<<<<< HEAD

from Deploy_ControlMemu import *
=======
from Deploy_ControlMemu import *

>>>>>>> bd8b1dad6e77b1f370cefeb1e57365b6070eee3f
from Deploy_ControlCommands import *

#####################################################
# Globals
<<<<<<< HEAD
SATAList = [["10.0.0.44",24441,"Status","Empty"],
			["10.0.0.44",24442,"Status","Empty"],
			["10.0.0.44",24443,"Status","Empty"]]
#SATAList = [["10.0.0.44",24441,"Status"],["10.0.0.44",24442,"Status"]]
=======
SATAList = [["10.0.0.44",8010,"Status"],["10.0.0.44",8020,"Status"],["10.0.0.44",8030,"Status"]]
>>>>>>> bd8b1dad6e77b1f370cefeb1e57365b6070eee3f

#####################################################
# Main Program
mmOption = "Go"

#Deply_Control_Setup()

while mmOption not in "qQ":
	
<<<<<<< HEAD
	mmOption = mnu_GetOption()
=======
	mmOption = Get_mmOption()
>>>>>>> bd8b1dad6e77b1f370cefeb1e57365b6070eee3f

	# Manage Clients
	##########################################
	if mmOption == "1":
		raw_input("Doing Option 1>")
<<<<<<< HEAD
		Satellites_Status(SATAList)
	elif mmOption == "2":
		raw_input("Doing Option 2>")	
		Satellites_SendCommand(SATAList)
=======
		Satalight_Status(SATAList)
	elif mmOption == "2":
		raw_input("Doing Option 2>")	
>>>>>>> bd8b1dad6e77b1f370cefeb1e57365b6070eee3f
	elif mmOption == "3":
		raw_input("Doing Option 3>")	
	elif mmOption == "4":
		raw_input("Doing Option 4>")	
	elif mmOption == "5":
		raw_input("Doing Option 5>")
<<<<<<< HEAD
	elif mmOption == "6":
		raw_input("Doing Option 6>")
		Satellite_Shut(SATAList)
=======
>>>>>>> bd8b1dad6e77b1f370cefeb1e57365b6070eee3f

#Deploy_Control_Close()

print "Goodbye...\n"


