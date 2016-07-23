#!/usr/bin/python
import os

SCR_Dir = os.path.dirname(__file__)

def mnu_ClrPrtHeader():
	with open(SCR_Dir+"/SCR-Control-MainMenu.scr") as mainF: mainS = mainF.read()
	os.system("clear")
	print mainS
	
def mnu_GetOption():
	Mpick = "A"
	while (Mpick not in "123456qQ") or Mpick=="":
		mnu_ClrPrtHeader()
		Mpick = raw_input("    Pick Option[#] or Q-uit> ")
	return Mpick

# Let the user pick a specific Satellite or All
#============================================================================
def mnu_PickSatallite(SAList):
	Lpick = "S"

	while (Lpick not in "1AaQq") or Lpick=="":
		mnu_ClrPrtHeader()
		print ("\tAvailable Satallite List:")
		for sal in range(0,len(SAList)):
			print "\t%s -Satalight: %s\t-Port: %s " % (str(sal),SAList[sal][0],SAList[sal][1])
		Lpick = raw_input("\n\tPick Satalite# to Command, A-All or Q-uit> ").strip().lstrip("0")
		if Lpick.isdigit() and (0<int(Lpick)<len(SAList)):
			Spick = Lpick
			Lpick = "1"
		elif (Lpick in "AaQq"):
			Spick = Lpick.upper()
	return Spick

# Let user select a acommand to be executed
#============================================================================
def mnu_GetCommand():

	Icommand = raw_input("\n\tEnter a Command or Q-uit> ").strip()
	
	return Icommand
